#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct the APS-2BM data saved as tiff using the Anka directory structure
"""

from __future__ import print_function

import os
import tomopy
import dxchange



if __name__ == '__main__':
    # Set tomobank id
    tomobank_id = 'tomo_00001'

    # Set path to the micro-CT data to reconstruct.
    fname = 'tomobank/datasets/' + tomobank_id + '/native_raw'

    proj_start = 2
    proj_end = 1503
    flat_start = 1
    flat_end = 2
    dark_start = 1504
    dark_end = 1505

    ind_tomo = range(proj_start, proj_end)
    ind_flat = range(flat_start, flat_end)
    ind_dark = range(dark_start, dark_end)

    # Select the sinogram range to reconstruct.
    start = 200
    end = 204

    # Read the APS 2-BM raw data.
    proj, flat, dark = dxchange.read_anka_topotomo(fname, ind_tomo, ind_flat,
                                                 ind_dark, sino=(start, end))

    # Set data collection angles as equally spaced between 0-180 degrees.
    theta = tomopy.angles(proj.shape[0], 0, 180)
   
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
    fname='tomobank/datasets/' + tomobank_id + '/rec_native/rec_native'
    dxchange.write_tiff_stack(rec, fname=fname)

