# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:35:30 2016

@author: decarlo
"""
from __future__ import (absolute_import, division, print_function,                        unicode_literals)
                        
from xdesign import *

import os
import timeimport pytzimport datetimeimport numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import dxfile.dxtomo as dx
import dxchange

def iso_time():
    # set the experiment date     now = datetime.datetime.today()

    # set iso format time    central = pytz.timezone('US/Central')    local_time = central.localize(now)    local_time_iso = local_time.isoformat()
    
    return local_time_iso

if __name__ == '__main__':

    # Set tomobank id
    tomobank_id = 'phantom_00001'

    # Set path to the micro-CT data to convert.
    fname = '/tomobank/phantoms/' + tomobank_id + '/' + tomobank_id + '.h5'    

    # Set meta-data
    experimenter_affiliation="Argonne National Laboratory" 
    experimenter_email="tomobank@anl.gov"
    instrument_name="XDesign VERSION:0.2.0.dev0+1d67599b8f104ebded86bac98100dbf15e251a66 FUNCTION: SlantedSquares(count=16, angle=5/360*2*np.pi, gap=0.01), prop='mass_atten'"  
    sample_name = tomobank_id

    # Phantom generation start time
    start_date = iso_time()

    phantom = SlantedSquares(count=16, angle=5/360*2*np.pi, gap=0.01)

    ccd_x = 256 
    ccd_y = 256
    n_proj = 512
    
    step = 1. / ccd_x    prb = Probe(Point([step / 2., -10]), Point([step / 2., 10]), step)

    n_dark = 1
    n_white = 1
    dark = np.zeros((n_dark, ccd_y, ccd_x)) # Array filled with zeros
    flat = np.ones((n_white, ccd_y, ccd_x)) # Array filled with ones

    sino = sinogram(n_proj, ccd_x, phantom)
    proj = np.expand_dims(sino, 1)

    # Theta
    theta_step = np.pi / n_proj    theta_step_deg = theta_step * 180./np.pi
    theta = np.arange(0, 180., 180. / n_proj)

    # Set data collection angles as equally spaced between 0-180 degrees.
    start_angle = 0
    start_angle_unit = 'deg'
    end_angle = 180
    end_angle_unit = 'deg'
    angular_step_unit = 'deg'

    # Phantom generation end time 
    end_date = iso_time()
                
    # Write ground_truth
    ground_truth = discrete_phantom(phantom, ccd_x, prop='mass_atten')
    fname_gt='/tomobank/phantoms/' + tomobank_id + '/' + tomobank_id + '_ground_truth'
    dxchange.write_tiff(ground_truth, fname=fname_gt, dtype='float32')

    # Save into a data-exchange file.
    if os.path.isfile(fname):
        print ("Data Exchange file already exists: ", fname)
    else:
        # Create new folder.
        dirPath = os.path.dirname(fname)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        # Open DataExchange file
        f = dx.File(fname, mode='w')
         
        # Write the Data Exchange HDF5 file.
        f.add_entry(dx.Entry.experimenter(affiliation={'value': experimenter_affiliation}))
        f.add_entry(dx.Entry.experimenter(email={'value': experimenter_email}))
        f.add_entry(dx.Entry.instrument(name={'value': instrument_name}))
        f.add_entry(dx.Entry.sample(name={'value': sample_name}))

        f.add_entry(dx.Entry.data(data={'value': proj, 'units':'counts'}))
        f.add_entry(dx.Entry.data(data_white={'value': flat, 'units':'counts'}))
        f.add_entry(dx.Entry.data(data_dark={'value': dark, 'units':'counts'}))
        f.add_entry(dx.Entry.data(theta={'value': theta, 'units':'degrees'}))
        f.add_entry(dx.Entry.data(ground_truth={'value': ground_truth, 'units':'counts'}))

        f.add_entry(dx.Entry.acquisition(start_date={'value': start_date}))
        f.add_entry(dx.Entry.acquisition(end_date={'value': end_date}))

        f.add_entry(dx.Entry.acquisition_setup(rotation_start_angle={'value': start_angle, 'unit': start_angle_unit}))
        f.add_entry(dx.Entry.acquisition_setup(rotation_end_angle={'value': end_angle, 'unit': end_angle_unit}))
        f.add_entry(dx.Entry.acquisition_setup(angular_step={'value': theta_step_deg, 'unit': angular_step_unit}))

        f.close()
        
       
        
