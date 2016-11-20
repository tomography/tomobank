#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct the APS-2BM data saved as dxchange
"""

from __future__ import print_function

import os
import tomopy
import dxchange



if __name__ == '__main__':
    # Set tomobank id
    tomobank_id = 'tomo_00001'

    # Set path to the micro-CT data to reconstruct.
    fname = 'tomobank/datasets/' + tomobank_id + '/' + tomobank_id + '.h5'

    # Select the sinogram range to reconstruct.
    start = 200
    end = 204

    # Read the APS 2-BM raw data.
    proj, flat, dark, theta = dxchange.read_aps_32id(fname, sino=(start, end))
    
    # Flat-field correction of raw data.
    proj = tomopy.normalize(proj, flat, dark)

    # Set rotation center.
    rot_center = 1024

    tomopy.minus_log(proj)

    # Reconstruct object using Gridrec algorithm.
    rec = tomopy.recon(proj, theta, center=rot_center, algorithm='gridrec', nchunk=1)

    # Mask each reconstructed slice with a circle.
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)

    # Write data as stack of TIFs.
    fname='tomobank/datasets/' + tomobank_id + '/rec_hdf/rec_hdf'
    dxchange.write_tiff_stack(rec, fname=fname)

