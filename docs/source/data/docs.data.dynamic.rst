Dynamic
-------

When setting a tomographic experiment several parameters are adjusted by the instrument operator 
including X-ray energy, exposure time, frame rate, rotary stage speed, scanning mode (sequential or 
interlaced angles etc.). Here we include a series of datasets collected at different experimental 
conditions aiming to capture fast evolving samples in 3D.


Noisy Data
~~~~~~~~~~

Sometimes data collection speed requirements, e. g. in evolving samples, impose very short 
exposure times generating noisy data.  Here we include a dataset, Dorthe_F_002, 
in which  the exposure time much shorter than the optimal value. 
The sample description and the experimental conditions are reported in tables below:
and accessible for download under tomo\_00031. 

To load the data sets and perform a basic reconstruction using `tomopy <https://tomopy.readthedocs.io>`_  use the 
:download:`tomopy_rec.py <../../demo/tomopy_rec.py>` python script.

Example: ::

    python tomopy_rec.py tomo_00031.h5 --axis 484.5

.. _tomo_00031: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2Ftomo_00031%2F

.. |00031| image:: ../img/tomo_00031.png
    :width: 20pt
    :height: 20pt

+------------------------+------------------------------------+
| tomo_ID                |       00031                        | 
+========================+====================================+
| Image preview          |      |00031|                       | 
+------------------------+------------------------------------+
| Downloads              |      tomo_00031_                   |  
+------------------------+------------------------------------+
| Instrument             |      APS 13-BM-D                   | 
+------------------------+------------------------------------+
| Sample name            |      Dorthe_F_002                  | 
+------------------------+------------------------------------+
| Energy                 |      33.269 keV                    | 
+------------------------+------------------------------------+
| Monochromator          |      double crystal Si (1,1,1)     |  
+------------------------+------------------------------------+
| Scan Range             |      180 degree                    | 
+------------------------+------------------------------------+
| Number of Projections  |      900                           | 
+------------------------+------------------------------------+
| White Fields           |      20 before                     | 
+------------------------+------------------------------------+
| Dark Fields            |      none                          |  
+------------------------+------------------------------------+
| Exposure Time          |      0.006 s                       | 
+------------------------+------------------------------------+
| Frame Rate             |      80 frames/s                   | 
+------------------------+------------------------------------+
| Total Collection Time  |      11.25 s                       | 
+------------------------+------------------------------------+
| PixelSize              |      3.18 µm                       | 
+------------------------+------------------------------------+
| Rotation axis location |      484.5                         |
+------------------------+------------------------------------+

Lower Resolution 
~~~~~~~~~~~~~~~~

This study was optimized for temporal resolution and less for spatial resolution. 
The experiment was originally designed to follow the propagation of a Cs solution 
with time in a rock. The spatial resolution could be relaxed at the time of 
the experiment to provide sufficient time resolution. 

In the second phase of the project, the focus moved however towards the smaller reactive 
inclusions and complementary techniques (x-ray microprobe and destructive chemical 
tomography with LA-ICP-MS) have been used to investigate the distribution of different elements
and phases in selected regions, with sometimes higher spatial resolution than in the original
tomographic dataset (see :cite:`gundlach:15`, :cite:`burger:15`).


To load the data sets and perform a basic reconstruction using `tomopy <https://tomopy.readthedocs.io>`_  use the 
:download:`tomopy_rec.py <../../demo/tomopy_rec.py>` python script.

Example: ::

    python tomopy_rec.py tomo_00069.h5 --axis 515.50

.. _tomo_00069: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2Ftomo_00069%2F

.. |00069| image:: ../img/tomo_00069.png
    :width: 20pt
    :height: 20pt

+-----------------------------+-------------------------------+
| tomo_ID                     |      00069                    | 
+=============================+===============================+
| Image preview               |     |00069|                   | 
+-----------------------------+-------------------------------+
| Downloads                   |     tomo_00069_               |  
+-----------------------------+-------------------------------+
| Instrument                  |     SLS TOMCAT                | 
+-----------------------------+-------------------------------+
| Sample name                 |     SLS_03/Cskin1_36__B1      | 
+-----------------------------+-------------------------------+
| Energy                      |     36.085 keV                | 
+-----------------------------+-------------------------------+
| Sample-to-detector distance |     4 mm                      |  
+-----------------------------+-------------------------------+
| Scan Range                  |     180 degree                | 
+-----------------------------+-------------------------------+
| Number of Projections       |     1001                      | 
+-----------------------------+-------------------------------+
| White Fields                |     20 (10 before - 10 after) | 
+-----------------------------+-------------------------------+
| Dark Fields                 |     5                         |  
+-----------------------------+-------------------------------+
| PixelSize                   |     3.7 µm                    | 
+-----------------------------+-------------------------------+
| Rotation axis location      |     515.500232028             |
+-----------------------------+-------------------------------+


Interlaced Scan
~~~~~~~~~~~~~~~

A technique adopted to capture fast evolving sample includes interlaced data collection.
In this mode multiple series of continuous 0-180 deg datasets are collected with 
equally spaced sparce angles. After each 0-180 deg rotation the next data set is collected 
with angular sampling interlaced to the previous scan.

Below we report the sample description and the experimental conditions for an interlace dataset
(tomo\_00057) :cite:`trabecular-bone:15`  collected at the Elettra Syrmep beamline.


.. _tomo_00057: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2Ftomo_00057%2F

.. |00057| image:: ../img/tomo_00057.png
    :width: 20pt
    :height: 20pt

+-----------------------------+---------------------------------------------------------+
| tomo_ID                     |       00057                                             | 
+=============================+=========================================================+
| Image preview               |      |00057|                                            | 
+-----------------------------+---------------------------------------------------------+
| Downloads                   |      tomo_00057_                                        |  
+-----------------------------+---------------------------------------------------------+
| Instrument                  |      Elettra Syrmep                                     |
+-----------------------------+---------------------------------------------------------+
| Sample name                 |      Bone MR                                            |
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



add MDB datasets 
~~~~~~~~~~~~~~~~

from  http://dx.doi.org/doi:10.18126/M2CC73

from  http://dx.doi.org/doi:10.18126/M2301J
