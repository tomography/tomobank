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
    Read array size of a specific group of Data Exchange file.

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


def read_rot_centers(fname):

    try:
        with open(fname) as json_file:
            json_string = json_file.read()
            dictionary = json.loads(json_string)

        return collections.OrderedDict(sorted(dictionary.items()))

    except Exception as error: 
        print("ERROR: the json file containing the rotation axis locations is missing")
        print("ERROR: run: python find_center.py to create one first")
        exit()


def reconstruct(h5fname, sino, rot_center, blocked_views=None):

    # Read APS 32-BM raw data.
    proj, flat, dark, theta = dxchange.read_aps_32id(h5fname, sino=sino)
        
    # Manage the missing angles:
    if blocked_views is not None:
        print("Blocked Views: ", blocked_views)
        proj = np.concatenate((proj[0:blocked_views[0],:,:], proj[blocked_views[1]+1:-1,:,:]), axis=0)
        theta = np.concatenate((theta[0:blocked_views[0]], theta[blocked_views[1]+1:-1]))

    # Flat-field correction of raw data.
    data = tomopy.normalize(proj, flat, dark, cutoff=1.4)

    # remove stripes
    data = tomopy.remove_stripe_fw(data,level=7,wname='sym16',sigma=1,pad=True)

    print("Raw data: ", h5fname)
    print("Center: ", rot_center)


    # Phase retrieval for tomobank id from 00032 to 00056
    # sample_detector_distance = 6.0
    # detector_pixel_size_x = 0.65e-4
    # monochromator_energy = 27.4

    # Phase retrieval for tomobank id 00058 and tomobank id 00059
    # sample_detector_distance = 6.0
    # detector_pixel_size_x = 0.65e-4
    # monochromator_energy = 27.4

    # Phase retrieval for tomobank id 00060 and tomobank id 00063
    # sample_detector_distance = 2.5
    # detector_pixel_size_x = 0.65e-4
    # monochromator_energy = 27.4

    # Phase retrieval for tomobank id 00064
    # sample_detector_distance = 0.8
    # detector_pixel_size_x = 1.4e-4
    # monochromator_energy = 55.0

    # Phase retrieval for tomobank id 00065
    # sample_detector_distance = 5.8
    # detector_pixel_size_x = 1.4e-4
    # monochromator_energy = 55.0

    # Phase retrieval for tomobank id 00066
    # sample_detector_distance = 15.8
    # detector_pixel_size_x = 1.4e-4
    # monochromator_energy = 55.0

    # Phase retrieval for tomobank id 00067
    # sample_detector_distance = 30.8
    # detector_pixel_size_x = 1.4e-4
    # monochromator_energy = 55.0

    # Phase retrieval for tomobank id 00068
    # sample_detector_distance = 15.0
    # detector_pixel_size_x = 4.1e-4
    # monochromator_energy = 14.0

    # Phase retrieval for tomobank id 00069
    # sample_detector_distance = 0.4 
    # detector_pixel_size_x = 3.7e-4
    # monochromator_energy = 36.085

    # Phase retrieval for tomobank id 00070
    # sample_detector_distance = 5.0
    # detector_pixel_size_x = 0.65e-4
    # monochromator_energy = 24.999

    # Phase retrieval for tomobank id 00071
    # sample_detector_distance = 1.5
    # detector_pixel_size_x = 0.65e-4
    # monochromator_energy = 24.999

    # Phase retrieval for tomobank id 00072
    # sample_detector_distance = 1.5
    # detector_pixel_size_x = 1.43e-4
    # monochromator_energy = 20.0

    # Phase retrieval for tomobank id 00073
    # sample_detector_distance = 1.0
    # detector_pixel_size_x = 0.74e-4
    # monochromator_energy = 25.0

    # Phase retrieval for tomobank id 00074
    # sample_detector_distance = 1.0
    # detector_pixel_size_x = 0.74e-4
    # monochromator_energy = 25.0

    # Phase retrieval for tomobank id 00075
    # sample_detector_distance = 11.0
    # detector_pixel_size_x = 1.43e-4
    # monochromator_energy = 60

    # Phase retrieval for tomobank id 00076
    # sample_detector_distance = 9.0
    # detector_pixel_size_x = 2.2e-4
    # monochromator_energy = 65

    # # phase retrieval
    # data = tomopy.prep.phase.retrieve_phase(data,pixel_size=detector_pixel_size_x,dist=sample_detector_distance,energy=monochromator_energy,alpha=8e-3,pad=True)

    data = tomopy.minus_log(data)

    data = tomopy.remove_nan(data, val=0.0)
    data = tomopy.remove_neg(data, val=0.00)
    data[np.where(data == np.inf)] = 0.00

    # Reconstruct object.
    rec = tomopy.recon(data, theta, center=rot_center, algorithm='gridrec')
        
    # Mask each reconstructed slice with a circle.
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)
    
    return rec
        

def rec_full(h5fname, rot_center, blocked_views):
    
    data_size = get_dx_dims(h5fname, 'data')

    # Select sinogram range to reconstruct.
    sino_start = 0
    sino_end = data_size[1]

    chunks = 16         # number of sinogram chunks to reconstruct
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
        rec = reconstruct(h5fname, sino, rot_center, blocked_views)
                
        # Write data as stack of TIFs.
        fname = os.path.dirname(h5fname) + '/' + os.path.splitext(os.path.basename(h5fname))[0]+ '_rec_full/' + 'recon'
        print("Reconstructions: ", fname)
        dxchange.write_tiff_stack(rec, fname=fname, start=strt)
        strt += sino[1] - sino[0]
    

def rec_slice(h5fname, nsino, rot_center, blocked_views):
    
    data_size = get_dx_dims(h5fname, 'data')
    ssino = int(data_size[1] * nsino)

    # Select sinogram range to reconstruct
    sino = None
        
    start = ssino
    end = start + 1
    sino = (start, end)

    # Reconstruct
    rec = reconstruct(h5fname, sino, rot_center, blocked_views)

    fname = os.path.dirname(h5fname) + '/' + os.path.splitext(os.path.basename(h5fname))[0]+ '_rec_slice/' + 'recon'
    dxchange.write_tiff_stack(rec, fname=fname)
    print("Rec: ", fname)
    print("Slice: ", start)
    
   
def main(arg):

    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="file name of a tmographic dataset: /data/sample.h5")
    parser.add_argument("--axis", nargs='?', type=str, default="0", help="rotation axis location: 1024.0 (default 1/2 image horizontal size)")
    parser.add_argument("--type", nargs='?', type=str, default="slice", help="reconstruction type: full (default slice)")
    parser.add_argument("--nsino", nargs='?', type=restricted_float, default=0.5, help="location of the sinogram used by slice reconstruction (0 top, 1 bottom): 0.5 (default 0.5)")

    args = parser.parse_args()

    # Set path to the micro-CT data to reconstruct.
    fname = args.fname

    rot_center = float(args.axis)

    # Set default rotation axis location
    if rot_center == 0:
        data_size = get_dx_dims(fname, 'data')
        rot_center =  data_size[2]/2

    nsino = float(args.nsino)

    blocked_views = None

    # Missing angles for tomobank id from 00007 to 00021
    # uncomment "blocked_views" for the dataset you want to reconstruct

    # tomo_00007 best_center = 1232; slice_first = 740; slice_last = 1700; 
    # blocked_views = [141,226]

    # tomo_00008 best_center = 1321; slice_first = 1000; slice_last = 1440; 
    # blocked_views = [141,228]

    # tomo_00009 best_center = 1219; slice_first = 550; slice_last = 1370; 
    # blocked_views = [147,233]

    # tomo_00010 best_center = 1286; slice_first = 740; slice_last = 1500; 
    # blocked_views = [142,227]

    # tomo_00011 best_center = 1292; slice_first = 620; slice_last = 1320; 
    # blocked_views = [140,226]

    # tomo_00012 best_center = 1116; slice_first = 800; slice_last = 1200; 
    # blocked_views = [140,225]

    # tomo_00013 best_center = 1314; slice_first = 610; slice_last = 1500; 
    # blocked_views = [71,113]

    # tomo_00014 best_center = 1140; slice_first = 610; slice_last = 1200; 
    # blocked_views = [140,226]

    # tomo_00015 best_center = 1124; slice_first = 740; slice_last = 1270; 
    # blocked_views = [140,227]

    # tomo_00016 best_center = 1338; slice_first = 760; slice_last = 1180; 
    # blocked_views = [140,227]

    # tomo_00017 best_center = 1232; slice_first = 710; slice_last = 1210; 
    # blocked_views = [140,227]

    # tomo_00018 best_center = 1292; slice_first = 700; slice_last = 1180; 
    # blocked_views = [138,225]

    # tomo_00019 best_center = 1114; slice_first = 740; slice_last = 1210; 
    # blocked_views = [141,228]

    # tomo_00020 best_center = 1352; slice_first = 750; slice_last = 1230; 
    # blocked_views = [138, 224]

    # tomo_00021 best_center = 1352; slice_first = 630; slice_last = 1100; 
    # blocked_views = [138, 224]



    slice = False
    if args.type == "slice":
        slice = True

    if os.path.isfile(fname):       
        if slice:             
            rec_slice(fname, nsino, rot_center, blocked_views)
        else:
            rec_full(fname, rot_center, blocked_views)

    else:
        print("File Name does not exist: ", fname)

if __name__ == "__main__":
    main(sys.argv[1:])

