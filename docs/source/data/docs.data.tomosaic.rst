Tomosaic
--------

Activated charcoal
~~~~~~~~~~~~~~~~~~

This dataset contains an activated charcoal sample that is approximately 4 mm in diameter. 
Since the sample extends beyond the field-of-view (FOV), the acquisition and reconstruction
were conducted using our Tomosaic protocol [1]. A full dataset stitched from a 4 by 4 mosaic
tile grid is available here.

Metadata files in the repository include:
.. * `center_pos.txt`: Center positions for each of the 4 rows of tiles.
.. * `shifts.txt`: Relative positions of all 16 tiles. The 6 columns in the file provide information
of: tile position y, tile position x, relative shift y to right neightbor, 
relative shift x to right neightbor, relative shift y to bottom neightbor, 
relative shift x to bottom neightbor.

Tomosaic, the software used to for processing and reconstructing the mosaic dataset, is an
open-source project which can be found here: tomosaic_



.. |00078| image:: ../img/tomo_00078.png
   :width: 20px
   :alt: project
   :align: center
.. _tomo_00078: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2F%2Ftomo_00078%2F
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

[1] R. Vescovi, M. Du, V. de Andrade, W. Scullin, D. Gursoy, and C. Jacobsen. (n.d.). Tomosaic: efficient acquisition and reconstruction of teravoxel tomography data using limited-size synchrotron x-ray beams. (Under review). 
