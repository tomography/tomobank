#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct a single data set.
"""

from __future__ import print_function

import os
import sys
import json
import argparse
import numpy as np
import collections

import h5py
import tomopy
import dxchange

   
def get_dx_dims(fname, dataset):
    """
    Read array size of a specific group of Data Exchange file.ls 

    Parameters
    ----------
    fname : str
        String defining the path of file or file name.
    dataset : str
        Path to the dataset inside hdf5 file where data is located.

    Returns
    -------
    ndarray
        Data set size.
    """

    grp = '/'.join(['exchange', dataset])

    with h5py.File(fname, "r") as f:
        try:
            data = f[grp]
        except KeyError:
            return None

        shape = data.shape

    return shape


def restricted_float(x):

    x = float(x)
    if x < 0.0 or x >= 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]"%(x,))
    return x

def reconstruct(h5fname, sino, nframes, frame, nproj, binning, tv, rot_center):

    # Read APS 32-BM raw data.
    print("Read data")
    proj, flat, dark, theta = dxchange.read_aps_32id(h5fname, sino=sino)

    print("Processing")
    if (frame-nframes)>0:
        proj = proj[(frame-nframes/2)*nproj:(frame+nframes/2)*nproj,:,:]

    # Flat-field correction of raw data.
    print("Flat-field correcting")
    data = tomopy.normalize(proj, flat, dark, cutoff=1.4)

    # remove stripes
    #print("Removing stripes")
    #data = tomopy.remove_stripe_fw(data,level=7,wname='sym16',sigma=1,pad=True)

    print("Raw data: ", h5fname)
    if (frame-nframes)>0:
        print("Frames for reconstruction:",(frame-nframes/2),"..",(frame+nframes/2))
    else:
        print("Frames for reconstruction:",(0),"..",(nframes))
    # Phase retrieval for tomobank id 00080
    # sample_detector_distance = 25
    # detector_pixel_size_x = 3.0e-4
    # monochromator_energy = 16

    # phase retrieval
    # data = tomopy.prep.phase.retrieve_phase(data,pixel_size=detector_pixel_size_x,dist=sample_detector_distance,energy=monochromator_energy,alpha=8e-03,pad=True)

    data = tomopy.minus_log(data)

    data = tomopy.remove_nan(data, val=0.0)
    data = tomopy.remove_neg(data, val=0.00)
    data[np.where(data == np.inf)] = 0.00

    # Binning 
    data = tomopy.downsample(data, level=binning, axis=2)
    if data.shape[1]>1:
       data = tomopy.downsample(data, level=binning, axis=1)

    theta = np.linspace(0,np.pi*nframes,nproj*nframes,endpoint=False)

    if tv:
	import rectv
	# Reconstruct. Iterative TV.
	[Ntheta,Nz,N] = data.shape
	Nzp = 4 # number of slices to process simultaniously by gpus
	M = nframes # number of basis functions, must be a multiple of nframes
	lambda0 = pow(2,-9) # regularization parameter 1
	lambda1 = pow(2,2) # regularization parameter 2 
	niters = 1024 # number of iterations
	ngpus = 1 # number of gpus

	data = np.ndarray.flatten(data.swapaxes(0,1)) # reorder input data for compatibility
	rec = np.zeros([N*N*Nz*M],dtype='float32') # memory for result

	# Make a class for tv
	cl = rectv.rectv(N,Ntheta,M,nframes,Nz,Nzp,ngpus,lambda0,lambda1)
	# Run iterations
	cl.itertvR_wrap(rec,data,niters) 

	rec = np.rot90(np.reshape(rec,[Nz,M,N,N]).swapaxes(0,1),axes=(2,3))/Ntheta*nframes*2 # reorder result for compatibility
	rec = rec[::M/nframes]
    else:
   	# Reconstruct object. FBP.
    	rec = np.zeros((nframes,data.shape[1],data.shape[2],data.shape[2]),dtype='float32')
	for time_frame in range(0,nframes):
		rec0 = tomopy.recon(data[time_frame*nproj:(time_frame+1)*nproj], theta[time_frame*nproj:(time_frame+1)*nproj], center=rot_center-np.mod(time_frame,2), algorithm='gridrec')        
		# Mask each reconstructed slice with a circle.
		rec[time_frame] = tomopy.circ_mask(rec0, axis=0, ratio=0.95)
    return rec
        

def rec_full(h5fname, nframes, frame, nproj, binning, tv, rot_center):
    
    data_size = get_dx_dims(h5fname, 'data')

    # Select sinogram range to reconstruct.
    sino_start = 0
    sino_end = data_size[1]

    chunks = data_size[1]/(8*pow(2,binning))         # number of sinogram chunks to reconstruct
                        # only one chunk at the time is reconstructed
                        # allowing for limited RAM machines to complete a full reconstruction

    nSino_per_chunk = (sino_end - sino_start)/chunks
    print("Reconstructing [%d] slices from slice [%d] to [%d] in [%d] chunks of [%d] slices each" % ((sino_end - sino_start), sino_start, sino_end, chunks, nSino_per_chunk))            

    strt = 0
    for iChunk in range(0,chunks):
        print('\n  -- chunk # %i' % (iChunk+1))
        sino_chunk_start = sino_start + nSino_per_chunk*iChunk 
        sino_chunk_end = sino_start + nSino_per_chunk*(iChunk+1)
        print('\n  --------> [%i, %i]' % (sino_chunk_start, sino_chunk_end))
                
        if sino_chunk_end > sino_end: 
            break

        sino = (int(sino_chunk_start), int(sino_chunk_end))

        # Reconstruct.
        rec = reconstruct(h5fname, sino, nframes, frame, nproj, binning, tv, rot_center)
                
        # Write data as stack of TIFs.
	for time_frame in range(0,nframes):
	        fname = os.path.dirname(os.path.abspath(h5fname)) + '/' + os.path.splitext(os.path.basename(h5fname))[0]+ '_rec_full/' + 'recon' + str(frame-nframes/2+time_frame) + '_'
	        print("Reconstructions: ", fname)	
	        dxchange.write_tiff_stack(rec[time_frame], fname=fname, start=strt)
        strt += (sino[1] - sino[0])/pow(2,binning)

def rec_subset(h5fname, nsino, nframes, frame, nproj, binning, tv, rot_center):
    
    data_size = get_dx_dims(h5fname, 'data')

    # Select sinogram range to reconstruct.
    ssino = int(data_size[1] * nsino)
    sino_start = ssino-4*pow(2,binning)
    sino_end = ssino+4*pow(2,binning)

    print("Reconstructing [%d] slices from slice [%d] to [%d]" % ((sino_end - sino_start), sino_start, sino_end))            

    sino = (int(sino_start), int(sino_end))
    # Reconstruct.
    rec = reconstruct(h5fname, sino, nframes, frame, nproj, binning, tv, rot_center)
           
    # Write data as stack of TIFs.
    for time_frame in range(0,nframes):
        fname = os.path.dirname(os.path.abspath(h5fname)) + '/' + os.path.splitext(os.path.basename(h5fname))[0]+ '_rec_subset/' + 'recon' + str(frame-nframes/2+time_frame) + '_'
        print("Reconstructions: ", fname)	
        dxchange.write_tiff_stack(rec[time_frame], fname=fname, start=sino_start)
    


def rec_slice(h5fname, nsino, nframes, frame, nproj, binning, tv, rot_center):
    
    data_size = get_dx_dims(h5fname, 'data')
    ssino = int(data_size[1] * nsino)

    # Select sinogram range to reconstruct
    sino = None
        
    start = ssino
    end = start + 1
    sino = (start, end)

    # Reconstruct
    rec = reconstruct(h5fname, sino, nframes, frame, nproj, binning, tv, rot_center)
    # Write data as stack of TIFs.

    for time_frame in range(0,nframes):
        if (frame-nframes)>0:
            fname = os.path.dirname(os.path.abspath(h5fname)) + '/' + os.path.splitext(os.path.basename(h5fname))[0]+ '_rec_slice/' + 'recon' + str(frame-nframes/2+time_frame) + '_'
        else:
	    fname = os.path.dirname(os.path.abspath(h5fname)) + '/' + os.path.splitext(os.path.basename(h5fname))[0]+ '_rec_slice/' + 'recon' + str(time_frame) + '_'
	dxchange.write_tiff_stack(rec[time_frame], fname=fname)
        print("Rec: ", fname)
    print("Slice: ", start)
    
   
def main(arg):

    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="file name of a tomographic dataset")
    parser.add_argument("--type", nargs='?', type=str, default="slice", help="reconstruction type: full (default slice)")
    parser.add_argument("--nsino", nargs='?', type=restricted_float, default=0.5, help="location of the sinogram used by slice reconstruction (0 top, 1 bottom): 0.5 (default 0.5)")
    parser.add_argument("--tv", nargs='?', type=bool, default=False, help="Use Total variation reconstruction method (Gridrec otherwise): False (default False)")
    parser.add_argument("--binning", nargs='?', type=str, default=0, help="binning projections: 0 (default 0)")
    parser.add_argument("--frame", nargs='?', type=str, default=92, help="time frame with motion: 92 (default 92)")
    parser.add_argument("--axis", nargs='?', type=str, default="0", help="rotation axis location: 1024.0 (default 1/2 image horizontal size)")
    parser.add_argument("--ntframes", nargs='?', type=str, default=60, help="total number of time frames (default 60)")
    parser.add_argument("--nproj", nargs='?', type=str, default=301, help="number of projections per time frame (default 301)")
    
    args = parser.parse_args()

    # Set path to the micro-CT data to reconstruct.
    fname = args.fname
    
    rot_center = float(args.axis)

    # Set default rotation axis location
    if rot_center == 0:
        data_size = get_dx_dims(fname, 'data')
        rot_center =  data_size[2]/2

    nsino = float(args.nsino)
    binning = int(args.binning)
    frame = int(args.frame)
    tv = args.tv

    print("Reconstructing with tv: " + str(tv))
    nframes = int(args.ntframes) #number of time frames for reconstruction
    nproj = int(args.nproj) #number of projections per 180 degrees interval
    
    slice = False
    subset = False

    if args.type == "slice":
        slice = True
    if args.type == "subset":
        subset = True


    if os.path.isfile(fname):       
        if slice:             
            rec_slice(fname, nsino, nframes, frame, nproj, binning, tv, rot_center)
	else: 
	    if subset:
	            rec_subset(fname, nsino, nframes, frame, nproj, binning, tv, rot_center)
	    else:
		    rec_full(fname, nframes, frame, nproj, binning, tv, rot_center)
    else:
        print("File Name does not exist: ", fname)

if __name__ == "__main__":
    main(sys.argv[1:])


