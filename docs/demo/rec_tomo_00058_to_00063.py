#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct tomo_00032 to tomo_00055 APS 2-BM 
"""

from __future__ import print_function

import tomopy
import dxchange

if __name__ == '__main__':


    sample_name = 'somya_20_60'
    tomo_id = 'tomo_00058'
    sample_detector_distance = 60
    rot_center = 1427

    sample_name = 'somya_30_60'
    tomo_id = 'tomo_00059'
    sample_detector_distance = 60
    rot_center = 1440
    
    sample_name = 'somya_30_25'
    tomo_id = 'tomo_00060'
    sample_detector_distance = 25
    rot_center = 1337

    sample_name = 'somya_20_25'
    tomo_id = 'tomo_00061'
    sample_detector_distance = 25
    rot_center = 1316.5
    
    sample_name = 'somya_10_25'
    tomo_id = 'tomo_00062'
    sample_detector_distance = 25
    rot_center = 1359.5
    
    sample_name = 'somya_5_25'
    tomo_id = 'tomo_00063'
    sample_detector_distance = 25
    rot_center =  1322.5  

    detector_pixel_size_x = 0.65e-4
    monochromator_energy = 27.4
       
    # Set path to the micro-CT data to reconstruct.
    fname = '/local/decarlo/data/tomobank/datasets/tomo_00058_to_00063/' + tomo_id + '.h5'

    # Select the sinogram range to reconstruct.
    start = 1022
    end = 1024

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
    dxchange.write_tiff_stack(rec, fname='recon_dir/aps_nik')
