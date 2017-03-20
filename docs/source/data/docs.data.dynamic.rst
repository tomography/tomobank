Dynamic
-------

When setting a tomographic experiment several parameters are adjusted by the instrument operator 
including X-ray energy, exposure time, frame rate, rotary stage speed, scanning mode (sequential or 
interlaced angles etc.). Here we include a series of datasets collected at different experimental 
conditions aiming to capture fast evolving samples in 3D.


Noisy Data
~~~~~~~~~~

Sometimes data collection speed requirements, e. g. in evolving samples, impose very short 
exposure times generating noisy data.  Noisy Data includes several data sets like Dorthe_F_002 in which 
the exposure time much shorter than the optimal value. 
The sample description and the experimental conditions are reported in tables below:
and accessible for download under tomo\_00031. 

+------------------------+---------------------------------------------------------+
| Instrument             |      APS 13-BM-D                                        |
+------------------------+---------------------------------------------------------+
| Energy                 |      33.269 keV                                         |
+------------------------+---------------------------------------------------------+
| Monochromator          |      double crystal Si (1,1,1)                          | 
+------------------------+---------------------------------------------------------+
| Scan Range             |      180 degree                                         |
+------------------------+---------------------------------------------------------+
| Number of Projections  |      900                                                |
+------------------------+---------------------------------------------------------+
| White Fields           |      20 before                                          |
+------------------------+---------------------------------------------------------+
| Dark Fields            |      none                                               | 
+------------------------+---------------------------------------------------------+
| Exposure Time          |      0.006 s                                            |
+------------------------+---------------------------------------------------------+
| Frame Rate             |      80 frames/s                                        |
+------------------------+---------------------------------------------------------+
| Total Collection Time  |      11.25 s                                            |
+------------------------+---------------------------------------------------------+
| PixelSize              |      3.18 µm                                            |
+------------------------+---------------------------------------------------------+

.. |tomo_00031| replace:: :download:`rec_script.py <../../../docs/demo/rec_tomo_00031.py>`


.. _tomo_00031: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2Ftomo_00031%2F

.. |00031| image:: ../img/tomo_00031.png
    :width: 20pt
    :height: 20pt

+-------------+------------------+-----------+-------------------------+
| Tomo ID     | Sample Name      |   Image   |       Downloads         |     
+-------------+------------------+-----------+-------------------------+ 
| tomo_00031_ |  Dorthe_F_002    |  |00031|  |      |tomo_00031|       |
+-------------+------------------+-----------+-------------------------+

Interlaced Scan
~~~~~~~~~~~~~~~

A technique adopted to capture fast evolving sample includes interlaced data collection.
In this mode multiple series of continuous 0-180 deg datasets are collected with 
equally spaced sparce angles. After each 0-180 deg rotation the next data set is collected 
with angular sampling interlaced to the previous scan.

Below we report the sample description and the experimental conditions for an interlace dataset
(tomo\_00031) collected at the Elettra Syrmep beamline.

+-----------------------------+---------------------------------------------------------+
| Instrument                  |      Elettra Syrmep                                     |
+-----------------------------+---------------------------------------------------------+
| Energy                      |      24 keV                                             |
+-----------------------------+---------------------------------------------------------+
| Filter                      |      1 mm Al                                            | 
+-----------------------------+---------------------------------------------------------+
| Sample-to-detector Distance |      210 mm                                             |
+-----------------------------+---------------------------------------------------------+
| Scan Range                  |      180 degree                                         |
+-----------------------------+---------------------------------------------------------+
| Interlaced Data Collection  |      20 projections x 36 (0-180 deg) iteration          |
+-----------------------------+---------------------------------------------------------+
| Total Projections           |      720                                                |
+-----------------------------+---------------------------------------------------------+
| White Fields                |      20                                                 |
+-----------------------------+---------------------------------------------------------+
| Dark Fields                 |      20                                                 | 
+-----------------------------+---------------------------------------------------------+
| Exposure Time               |      0.8 s                                              |
+-----------------------------+---------------------------------------------------------+

.. |tomo_00057| replace:: :download:`rec_script.py <../../../docs/demo/rec_tomo_00057.py>`


.. _tomo_00057: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2Ftomo_00057%2F

.. |00057| image:: ../img/tomo_00057.png
    :width: 20pt
    :height: 20pt

+-------------+------------------+-----------+-------------------------+
| Tomo ID     | Sample Name      |   Image   |       Downloads         |     
+-------------+------------------+-----------+-------------------------+ 
| tomo_00057_ |  Bone MR         |  |00057|  |      |tomo_00057|       |
+-------------+------------------+-----------+-------------------------+

add datasets SLS03 
~~~~~~~~~~~~~~~~~~

from https://drive.google.com/drive/folders/0B78bW1AwveI_WVdXQlBRMVBKQk0

add datasets MDB
~~~~~~~~~~~~~~~~

from  http://dx.doi.org/doi:10.18126/M2CC73

from  http://dx.doi.org/doi:10.18126/M2301J
