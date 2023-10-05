#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python example of how to read am images.
"""

from __future__ import print_function
import os
import sys
import argparse
import fnmatch
import tomopy
import dxchange
import numpy as np


from os.path import expanduser

   
def main(arg):
    # Set tomobank id
    tomobank_id = 'tomo_00025'

    # Set path to the micro-CT data to reconstruct.
    fname = 'tomobank/' + tomobank_id + '/native/' + tomobank_id + '.h5'
    
    # Read the hdf raw data.
    sino, sflat, sdark, th = dxchange.read_aps_32id(fname)

    # Set data collection angles as equally spaced between 0-180 degrees.
    theta = tomopy.angles(sino.shape[1], ang1=0.0, ang2=180.0)

    print(sino.shape, sdark.shape, sflat.shape, theta.shape)

    # Quick normalization just to see something ....
    ndata = sino / float(np.amax(sino))
    slider(ndata)

    # Find rotation center.
    rot_center = 952

    binning = 1
    ndata = tomopy.downsample(ndata, level=int(binning))
    rot_center = rot_center/np.power(2, float(binning))    

    ndata = tomopy.minus_log(ndata)
    
    # Reconstruct object using Gridrec algorithm.
    rec = tomopy.recon(ndata, theta, center=rot_center, sinogram_order=True, algorithm='gridrec')

    # Mask each reconstructed slice with a circle.
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)

    # Write data as stack of TIFs.
    dxchange.write_tiff_stack(rec, fname='recon_dir/recon')

if __name__ == "__main__":
    main(sys.argv[1:])
