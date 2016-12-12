#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct a phantom dataset saved as dxchange
"""

from __future__ import print_function

import os
import tomopy
import dxchange

if __name__ == '__main__':
    # Set tomobank id
    tomobank_id = 'phantom_00008'

    # Set path to the micro-CT data to reconstruct.
    fname = '/tomobank/phantoms/' + tomobank_id + '/' + tomobank_id + '.h5'

    # Select the sinogram range to reconstruct.
    start = 0
    end = 1

    # Read the APS 2-BM raw data.
    proj, flat, dark, theta = dxchange.read_aps_32id(fname, sino=(start, end))
    
    # Flat-field correction of raw data.
    proj = tomopy.normalize(proj, flat, dark)

    # Set rotation center.
    rot_center = (proj.shape[2]-1)/2.
    print (rot_center)
    
    
    tomopy.minus_log(proj)

    # Reconstruct object using Gridrec algorithm.
    rec = tomopy.recon(proj, theta, center=rot_center, algorithm='gridrec', nchunk=1)

    # Mask each reconstructed slice with a circle.
    #rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)
    
    # Write data as stack of TIFs.
    fname='/tomobank/phantoms/' + tomobank_id + '/' + tomobank_id
    dxchange.write_tiff_stack(rec, fname=fname)

