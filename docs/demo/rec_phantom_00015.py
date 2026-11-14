#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rectv
import numpy as np
import dxchange
import tomopy 
import sys

def rec_tv(data,m,nsp,rot_center,
           lambda0,lambda1,niters,ngpus):
    """
    Reconstruct. Time-domain decomposition + regularization.
    """

    [nframes, nproj, ns, n] = data.shape

    # cut data according to the rotation center    
    if (rot_center<n//2):
        data = data[:,:,:,:n//2+rot_center-1]
    if (rot_center>n//2):
        data = data[:,:,:,rot_center-n//2:]
    n = data.shape[3]

    # reorder input data for compatibility
    data = np.reshape(data,[nframes*nproj,ns,n])
    data = np.ndarray.flatten(data.swapaxes(0, 1))
    
    # memory for result
    rec = np.zeros([n*n*ns*m], dtype='float32')  

    # Make a class for tv
    cl = rectv.rectv(n, nframes*nproj, m, nframes, ns,
                     ns, ngpus, lambda0, lambda1)
    # Run iterations
    cl.itertvR_wrap(rec, data, niters)

    # reorder result for compatibility with tomopy
    rec = np.rot90(np.reshape(rec, [ns, m, n, n]).swapaxes(0, 1), axes=(
        2, 3))/nproj*2 
    
    # take slices corresponding to angles k\pi
    rec = rec[::m//nframes]
    for time_frame in range(0, nframes):
        # Mask each reconstructed slice with a circle.
        rec[time_frame] = tomopy.circ_mask(rec[time_frame], axis=0, ratio=0.95)

    return rec

def rec(data,rot_center):
    """
    Reconstruct with Gridrec.
    """

    [nframes, nproj, ns, n] = data.shape
    theta = np.linspace(0, np.pi*nframes, nproj*nframes, endpoint=False)
    # Reconstruct object. FBP.
    rec = np.zeros([nframes, ns, n, n], dtype='float32')
    for time_frame in range(0, nframes):
        rec0 = tomopy.recon(data[time_frame], theta[time_frame*nproj:(time_frame+1)*nproj], center=rot_center, algorithm='gridrec')
        # Mask each reconstructed slice with a circle.
        rec[time_frame] = tomopy.circ_mask(rec0, axis=0, ratio=0.95)
    
    return rec

if __name__ == "__main__":

    # read 8 time frames of data
    data = dxchange.reader.read_tiff_stack(sys.argv[1],ind=np.arange(0,8))
    # add dimension for slices
    data = np.expand_dims(data,2)

    rot_center = 128 # rotation center

    # 1) reconstruct  by gridrec
    r = rec(data,rot_center)

    for k in range(r.shape[0]):
        dxchange.write_tiff_stack(r[k],'recfbp/recfbp_'+str(k))


    # 2) reconstruct by the time-domain decomposition + regularization
    nsp = 1  # number of slices to process simultaniously by gpus
    niters = 1024  # number of iterations
    ngpus = 1  # number of gpus  
    m = 16# number of basis functions, must be a multiple of nframes
    lambda0 = pow(2, -9)  # regularization parameter 1
    lambda1 = pow(2, 1)  # regularization parameter 2

    rtv = rec_tv(data,m,nsp,rot_center,lambda0,lambda1,niters,ngpus)
    for k in range(rtv.shape[0]):
        dxchange.write_tiff_stack(rtv[k],'rectv/recb16tv_'+str(k))

