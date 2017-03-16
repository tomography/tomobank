#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct the Elettra data saved as dxchange
"""

from __future__ import print_function

import os
import tomopy
import dxchange
import numpy as np

if __name__ == '__main__':
    # Set tomobank id
    tomobank_id = 'tomo_00022'

    # Set path to the micro-CT data to reconstruct.
    fname = '/tomobank/datasets/' + tomobank_id + '/' + tomobank_id + '.h5'

    proj, flat, dark, theta = dxchange.read_aps_32id(fname)

    if (theta is None):
        theta = tomopy.angles(proj.shape[1])
    else:
        theta = theta * np.pi / 180.

    proj = np.swapaxes(proj, 0, 1)
    flat = np.swapaxes(flat, 0, 1)
    dark = np.swapaxes(dark, 0, 1)

    # Select the sinogram range to reconstruct.
    start = 1024
    end = 1025
    proj = proj[:, [start,end], :]
    flat = flat[:, [start,end], :]
    dark = dark[:, [start,end], :]   
    
    # Flat-field correction of raw data.
    proj = tomopy.normalize(proj, flat, dark)

    # Set rotation center.
    rot_center = 980

    proj = tomopy.minus_log(proj)

    # Reconstruct object using Gridrec algorithm.
    rec = tomopy.recon(proj, theta, center=rot_center, algorithm='gridrec', nchunk=1)

    # Mask each reconstructed slice with a circle.
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)

    # Write data as stack of TIFs.
    fname='/tomobank/datasets/' + tomobank_id + '/' + tomobank_id
    dxchange.write_tiff_stack(rec, fname=fname)

