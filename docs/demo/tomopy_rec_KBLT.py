#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct a single KBLT data sets.
Author: Emanuel Larsson, Lund University, Lund, Sweden
email: emanuel.larsson@solid.lth.se
"""

from __future__ import print_function

import os
import sys
import numpy as np
from numpy import inf

import h5py
import tomopy
import dxchange

import tomopy.util.mproc as mproc
import tomopy.util.dtype as dtype
import numexpr as ne

from skimage.color import rgb2gray
from skimage.util import img_as_uint, img_as_ubyte, img_as_float32
from skimage.transform import rotate

def kblt_normalize(arr, flat, cutoff=None, ncore=None, out=None):
    """
    Normalize raw projection KBLT data using only the flat field projections.
    
    This function is a modified version of the following function from TomoPy:
    https://tomopy.readthedocs.io/en/latest/api/tomopy.prep.normalize.html#tomopy.prep.normalize.normalize

    Parameters
    ----------
    arr : ndarray
        3D stack of projections.
    flat : ndarray
        3D flat field data.
    cutoff : float, optional
        Permitted maximum vaue for the normalized data.
    ncore : int, optional
        Number of cores that will be assigned to jobs.
    out : ndarray, optional
        Output array for result. If same as arr,
        process will be done in-place.

    Returns
    -------
    ndarray
        Normalized 3D KBLT tomographic data.
    """
    arr = dtype.as_float32(arr)
    l = np.float32(1e-6)
    flat = np.mean(flat, axis=0, dtype=np.float32)

    with mproc.set_numexpr_threads(ncore):
        denom = ne.evaluate('flat')
        ne.evaluate('where(denom<l,l,denom)', out=denom)
        out = ne.evaluate('arr', out=out)
        ne.evaluate('out/denom', out=out, truediv=True)
        if cutoff is not None:
            cutoff = np.float32(cutoff)
            ne.evaluate('where(out>cutoff,cutoff,out)', out=out)
    return out 
   
def main(arg):

    #sample names of datasets to reconstruct
    
    sample = '1_plastic_screw_RGB'
    tilt = 1.4
    angle = 360
    rot_center_user = 104.75
    
    #sample = '2_plastic_beeds_RGB'
    #tilt = -0.6
    #angle = 360
    #rot_center_user = 65
    
    #sample = '3_legoman_RGB'
    #tilt = 1.2
    #angle = 360
    #rot_center_user = 180

    #sample = '4_fairy_slime_RGB'
    #tilt = 0
    #angle = 360
    #rot_center_user = 174.5
    
    #sample = '5A_seeds_drink_1st_light_RGB'
    #tilt = -0.6
    #angle = 360
    #rot_center_user = 158.5

    #sample = '5B_seeds_drink_2nd_light_RGB'
    #tilt = -0.3
    #angle = 360
    #rot_center_user = 164.25

    #sample = '6_hourglass_RGB'
    #tilt = 0.4
    #angle = 360
    #rot_center_user = 93
    #rep = 'rep_01'
    
    #sample = '7_chocolate_RGB'
    #tilt = 0
    #angle = 360
    #rot_center_user = 198.75
    #rep = 'rep_02'

    #sample = '8_lavalamp_RGB'
    #tilt = 0
    #angle = 180
    #rot_center_user = 319.25
    #rep = 'rep_15'

    #folders
    fname = 'C:/Users/Emanuel Larsson/Desktop/KBLT/DATA_SETS/h5_data_sets_JMTS/'
    #fname = 'E:/KBLT/lava_dyn7/180_scans/'
    fname_in = fname + str(sample) + '.h5'
    fname_out = os.path.join( fname + str(sample) + '/' )
    
    print(fname_out)
    
    #create the output folder
    if not os.path.exists(fname_out):
        os.makedirs(fname_out)

    #read in the h5 dataset (in RGB format)
    hf = h5py.File(fname_in, 'r')
    flat = hf.get('flat')
    
    #for 3D KBLT only one tomo exists. For 4D several repetitive tomos over time exist.
    if 'rep' in locals():
        print('4D KBLT dataset!')
        tomo = hf.get('tomo/' + rep)
    else:
        print('3D KBLT dataset!')
        tomo = hf.get('tomo')

    #convert to numpy array
    tomo = np.array(tomo)
    flat = np.array(flat)
    
    #convert from RGB to 16 bit grey scale level
    #individual user defined conversion value, depending on the lightening conditions
    conversion_factor = 32767
    tomo = rgb2gray(tomo) * conversion_factor
    tomo = tomo.astype(np.int16)
    flat = rgb2gray(flat) * conversion_factor
    flat = flat.astype(np.int16)

    #Normalize the projection images
    data = kblt_normalize(tomo, flat)

    #Set potentiall +/-infinity to either 0 or 1 respectively
    data[np.isnan(data)] = 0
    data[data == -inf] = 0
    data[data == inf] = 1
    data = tomopy.minus_log(data)

    #if the defined tilt is not zero, then correct the tilt for the respecive datasets
    if tilt is not 0:

        #convert 16 bit flat-fielded projections to 32 bit projections for higher accuracy
        #data=img_as_float32(data)

        #tilt correct the flat-fielded projections
        for i in range(len(data)):
            data[i] = rotate(data[i], angle=tilt, resize=False, center=None, order=1, mode='constant', cval=0, clip=True, preserve_range=False)

        #convert back from 32 bit to 16 bit
        #data=img_as_uint(data)
        
        print('tilt correction done!')
        
    else:
        print('skipped tilt correction!')

    #define scanning angles
    theta = tomopy.angles(data.shape[0], 0, angle)
    
    #center of rotation in the middle of the image
    rot_center = (data.shape[2]) / 2.0
    print('The central point of the image is: ' + str(rot_center))
    rot_center = tomopy.find_center_pc(data[0], data[-1], tol=0.5, rotc_guess=rot_center)
    print('The automatically detected CoR is: ' + str(rot_center))
    rot_center = rot_center_user
    print('User-defined CoR is: ' + str(rot_center))

    #define slices to reconstruct
    slice_start = 0
    slice_end = len(data[0])
    #slice_start = 200
    #slice_end = 300

    #reconstruct slices
    rec = tomopy.recon(data[:, slice_start:slice_end, :], theta=theta, center=rot_center, algorithm='gridrec')

    #set pixels outside the circle to zero
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)

    fname_out_tiff = os.path.join( fname_out + '/rec_cr_' + str(rot_center_user) + '/')

    #for writing out repetitive reconstructions as individual files
    if 'rep' in locals():
        fname_out_tiff = fname_out_tiff + '/' + str(rep) + '/'
        fname_out_hdf5 = fname_out + str(sample) + '_' + str(rep) + '_cr_' + str(rot_center_user) + '.h5'
    else:
        fname_out_hdf5 = fname_out + str(sample) + '_cr_' + str(rot_center_user) + '.h5'

    print(fname_out_hdf5)

    #create final output folder
    if not os.path.exists(fname_out_tiff):
        os.makedirs(fname_out_tiff)
    
    #save out the reconstructed volume as a tiff stack
    dxchange.write_tiff_stack(rec[:, :, :], fname = fname_out_tiff + 'slice')

    #save out the reconstructed volume as a single h5 file
    dxchange.writer.write_dxf(rec, fname=fname_out_hdf5, axes=u'theta:y:x', dtype=None, overwrite=False)
    
if __name__ == "__main__":
    main(sys.argv[1:])

