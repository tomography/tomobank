Wet Circles
-----------

.. |rec00007| image:: ../img/phantom_00007_00000.png
    :width: 20pt
    :height: 20pt

.. |gt00007| image:: ../img/phantom_00007_ground_truth.png
    :width: 20pt
    :height: 20pt

.. |phan_00007| replace:: :download:`gen_script.py <../../../docs/demo/phantom_00007.py>`

.. _phan_00007: https://app.globus.org/file-manager?origin_id=9f00a780-4aee-42a7-b7f4-6a2773c8da30&origin_path=%2Fphantom_00007%2F

These phantom use `XDesign <http://myxdesign.readthedocs.io/>`_ 
version `0.2.0.dev0+1d67599 <https://github.com/tomography/xdesign/tree/1d67599b8f104ebded86bac98100dbf15e251a66>`_
are generated as follows:     


.. code:: python

    ccd_x = 256 
    ccd_y = 1
    n_proj = 512

    phantom_00007 = xdesign.WetCircles()

The ground truth, sinogram and projection are obtained with:

.. code:: python

    ground_truth = discrete_phantom(phantom, ccd_x, prop='mass_atten')
    
    sino, probe = sinogram(n_proj, ccd_x, phantom)
    proj = np.expand_dims(sino, 1)

To load the phantom data sets and perform a basic reconstruction using `tomopy <https://tomopy.readthedocs.io>`_  use the 
:download:`tomopy_rec.py <../../demo/tomopy_rec.py>` python script:

::

    tomopy recon --file-name phantom_00007.h5

+---------------+----------------+------------------------+--------------+------------+--------------------+
|  Phantom ID   |    Facility    |    Sample              | Ground Truth |  Grirec    |       Downloads    |
+---------------+----------------+------------------------+--------------+------------+--------------------+
| phan_00007_   |    XDesign     |  Wet Circles           |  |gt00007|   | |rec00007| |      |phan_00007|  |
+---------------+----------------+------------------------+--------------+------------+--------------------+


