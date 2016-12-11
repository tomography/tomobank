Foam----

.. |rec00008| image:: ../img/phantom_00008_00000.png
    :width: 20pt
    :height: 20pt

.. |gt00008| image:: ../img/phantom_00008_ground_truth.png
    :width: 20pt
    :height: 20pt

.. |phan_00008| replace:: :download:`script.py <../../../docs/demo/phantom_00008.py>`


.. _phan_00008: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2F/


.. |rec00009| image:: ../img/phantom_00009_00000.png
    :width: 20pt
    :height: 20pt

.. |gt00009| image:: ../img/phantom_00009_ground_truth.png
    :width: 20pt
    :height: 20pt

.. |phan_00009| replace:: :download:`script.py <../../../docs/demo/phantom_00009.py>`


.. _phan_00009: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2F/

.. |rec00010| image:: ../img/phantom_00010_00000.png
    :width: 20pt
    :height: 20pt

.. |gt00010| image:: ../img/phantom_00010_ground_truth.png
    :width: 20pt
    :height: 20pt

.. |phan_00010| replace:: :download:`script.py <../../../docs/demo/phantom_00010.py>`


.. _phan_00010: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2F/

.. |rec00011| image:: ../img/phantom_00011_00000.png
    :width: 20pt
    :height: 20pt

.. |gt00011| image:: ../img/phantom_00011_ground_truth.png
    :width: 20pt
    :height: 20pt

.. |phan_00011| replace:: :download:`script.py <../../../docs/demo/phantom_00011.py>`


.. _phan_00011: https://www.globus.org/app/transfer?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2F/


These phantom use `XDesign <http://myxdesign.readthedocs.io/>`_ 
version `0.2.0.dev0+1d67599 <https://github.com/tomography/xdesign/tree/1d67599b8f104ebded86bac98100dbf15e251a66>`_
are generated as follows:     


.. code:: python

    ccd_x = 256 
    ccd_y = 1
    n_proj = 512

    phantom_00008 = xdesign.Foam(size_range=[0.05, 0.01], gap=0, porosity=1)
    phantom_00009 = xdesign.Foam(size_range=[0.07, 0.01], gap=0, porosity=0.75)
    phantom_00010 = xdesign.Foam(size_range=[0.1, 0.01], gap=0, porosity=0.5)
    phantom_00011 = xdesign.Foam(size_range=[0.1, 0.01], gap=0.015, porosity=0.5)
    
The ground truth, sinogram and projection are obtained with:

.. code:: python

    ground_truth = discrete_phantom(phantom, ccd_x, prop='mass_atten')
    
    sino = sinogram(n_proj, ccd_x, phantom)
    proj = np.expand_dims(sino, 1)

+---------------+----------------+------------------------+--------------+------------+-------------------------+-------------------------+
|  Phantom ID   |    Facility    |    Sample              | Ground Truth |  Grirec    |                     Downloads                     |                             
+---------------+----------------+------------------------+--------------+------------+-------------------------+-------------------------+
|     00008     |    XDesign     |  Foam 00008            |  |gt00008|   | |rec00008| |      |phan_00008|       |       phan_00008_       |
+---------------+----------------+------------------------+--------------+------------+-------------------------+-------------------------+
|     00009     |    XDesign     |  Foam 00009            |  |gt00009|   | |rec00009| |      |phan_00009|       |       phan_00009_       |
+---------------+----------------+------------------------+--------------+------------+-------------------------+-------------------------+
|     00010     |    XDesign     |  Foam 00010            |  |gt00010|   | |rec00010| |      |phan_00010|       |       phan_00010_       |
+---------------+----------------+------------------------+--------------+------------+-------------------------+-------------------------+
|     00011     |    XDesign     |  Foam 00011            |  |gt00011|   | |rec00011| |      |phan_00011|       |       phan_00011_       |
+---------------+----------------+------------------------+--------------+------------+-------------------------+-------------------------+


