#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct tomo_00032 to tomo_00055 APS 2-BM 
"""

from __future__ import print_function

import tomopy
import dxchange

if __name__ == '__main__':


    tomo_id = 'tomo_00064'
    sample_detector_distance = 8
    rot_center = 175

    #tomo_id = 'tomo_00065'
    #sample_detector_distance = 58
    #rot_center = 175
    
    #tomo_id = 'tomo_00066'
    #sample_detector_distance = 158
    #rot_center = 175

    #tomo_id = 'tomo_00067'
    #sample_detector_distance = 308
    #rot_center = 175
    
    detector_pixel_size_x = 1.4e-4
    monochromator_energy = 55.0
       
    # Set path to the micro-CT data to reconstruct.
    fname = '/tomobank/tomo_00064_to_00067/' + tomo_id + '.h5'

    # Select the sinogram range to reconstruct.
    start = 122
    end = 124

    sino=(start, end)

    # Read raw data.
    proj, flat, dark, theta = dxchange.read_aps_32id(fname, sino=(start, end))

    # Flat-field correction of raw data.
    data = tomopy.normalize(proj, flat, dark)

    # remove stripes    
    data = tomopy.prep.stripe.remove_stripe_fw(data,level=5,wname='sym16',sigma=1,pad=True)

    # phase retrieval
    data = tomopy.prep.phase.retrieve_phase(data,pixel_size=detector_pixel_size_x,dist=sample_detector_distance,energy=monochromator_energy,alpha=8e-3,pad=True)

    # Set rotation center.
    rot_center = rot_center

    data = tomopy.minus_log(data)

    # Reconstruct object using Gridrec algorithm.
    rec = tomopy.recon(data, theta, center=rot_center, algorithm='gridrec')

    # Mask each reconstructed slice with a circle.
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)

    # Write data as stack of TIFs.
    dxchange.write_tiff_stack(rec, fname='recon_dir/esrf')
