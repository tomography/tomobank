#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TomoPy example script to reconstruct tomo_00032 to tomo_00056 APS 2-BM 
"""

from __future__ import print_function

import tomopy
import dxchange

if __name__ == '__main__':


    sample_name = 'H14_7075PA_172HV_99NF'

    #fatigue_cycle = '00750'
    #fatigue_cycle = '01500'
    #fatigue_cycle = '02000'
    #fatigue_cycle = '02750'
    #fatigue_cycle = '03500'
    #fatigue_cycle = '04000'
    #fatigue_cycle = '04500'
    #fatigue_cycle = '05500'
    #fatigue_cycle = '06500'
    #fatigue_cycle = '07500'
    #fatigue_cycle = '08500'
    fatigue_cycle = '10000'
    #fatigue_cycle = '12000'
    #fatigue_cycle = '13000'
    #fatigue_cycle = '13100'
    #fatigue_cycle = '13200'
    #fatigue_cycle = '13300'
    #fatigue_cycle = '13400'
    #fatigue_cycle = '13800'
    #fatigue_cycle = '13900'
    #fatigue_cycle = '14000'
    #fatigue_cycle = '14100'
    #fatigue_cycle = '14200'
    #fatigue_cycle = '14300'
    #fatigue_cycle = '14346'
    print (sample_name + fatigue_cycle)
            
    sample_detector_distance = 60

    detector_pixel_size_x = 0.65e-4
    monochromator_energy = 27.4
       
    # Set path to the micro-CT data to reconstruct.
    fname = '/local/decarlo/data/tomobank/' + sample_name + '_' + fatigue_cycle + 'C'  + '.h5'

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
    rot_center = 1235

    data = tomopy.minus_log(data)

    # Reconstruct object using Gridrec algorithm.
    rec = tomopy.recon(data, theta, center=rot_center, algorithm='gridrec')

    # Mask each reconstructed slice with a circle.
    rec = tomopy.circ_mask(rec, axis=0, ratio=0.95)

    # Write data as stack of TIFs.
    dxchange.write_tiff_stack(rec, fname='recon_dir')