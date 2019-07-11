Mosaic
------



Activated charcoal
~~~~~~~~~~~~~~~~~~

This dataset contains an activated charcoal sample that is approximately 4 mm in diameter. 
Since the sample extends beyond the field-of-view (FOV), the acquisition and reconstruction
were conducted using the Tomosaic protocol [ref]. A full dataset stitched from a 4 by 4 mosaic
tile grid is available here.

Tomosaic, the software used to for processing and reconstructing the mosaic dataset, is an
open-source project which can be found here: tomosaic_

Metadata files in the repository include:
  * `center_pos.txt`: Center axis positions for each of the 4 rows of tiles.
  * `shifts.txt`: Relative positions of all 16 tiles. The 6 columns in the file provide information

of: tile position y, tile position x, relative shift y to right neightbor, 
relative shift x to right neightbor, relative shift y to bottom neightbor, 
relative shift x to bottom neightbor.


.. |00078| image:: ../img/tomo_00078.png
    :width: 20pt
    :height: 20pt

.. _tomo_00078: https://app.globus.org/file-manager?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2F%2Ftomo_00078%2F

.. _tomosaic: https://github.com/mdw771/tomosaic2.git

+-----------------------------------------+----------------------------+
|             tomo_ID                     | 00078                      |  
+=========================================+============================+
|             Image preview               | |00078|                    |  
+-----------------------------------------+----------------------------+
|             Download                    | tomo_00078_                |  
+-----------------------------------------+----------------------------+
|             Instrument                  | APS 32-ID-C                |  
+-----------------------------------------+----------------------------+
|             Sample name                 | Charcoal                   |  
+-----------------------------------------+----------------------------+
|             X-ray energy                | 25.0 keV                   |  
+-----------------------------------------+----------------------------+
|             Sample-to-detector distance | 30 cm                      |  
+-----------------------------------------+----------------------------+
|             Scan Range                  | 180 degree                 |
+-----------------------------------------+----------------------------+
|             Number of Projections       | 4500                       |
+-----------------------------------------+----------------------------+
|             White Fields                | 50                         | 
+-----------------------------------------+----------------------------+
|             Dark Fields                 | 10                         |  
+-----------------------------------------+----------------------------+
|             Pixel size                  | 0.8 um                     |  
+-----------------------------------------+----------------------------+
|             Mosaic tile grid            | 4 x 4                      |
+-----------------------------------------+----------------------------+
|             FOV size                    | 1920 x 1200                |
+-----------------------------------------+----------------------------+
|             Stitched panorama size      | 6618 x 4205                |
+-----------------------------------------+----------------------------+
|             Rotation axis location      | See globus                 |
+-----------------------------------------+----------------------------+

To load the data sets and perform a basic reconstruction using `tomopy <https://tomopy.readthedocs.io>`_  use the 
:download:`tomopy_rec.py <../../demo/tomopy_rec.py>` python script. Check `center_pos.txt` for rotation axis positions.

Example: ::

    python tomopy_rec.py tomo_00078.h5 --axis 3316

To enable phase retrieval un-comment the appropriate setting in :download:`tomopy_rec.py <../../demo/tomopy_rec.py>` 

To find the correct axis value in `center_pos.txt` to use, you need to first figure out which row the slice you want
to reconstruct belong to. You can do this with the aid of `shifts.txt`. For example, the y-shift of the second row
of tile relative to the first row is 997, and that of the third row relative to the second row is 996. So slice
997 to 1993 will be on the second row, corresponding to an axis of 3324. The most convenient way to reconstruct
this dataset is to use the `recon_hdf5` function in Tomosaic. The source codes of Tomosaic can be found here: tomosaic_
