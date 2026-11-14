Phantoms
========

All phantom data sets are generated with `XDesign <http://xdesign.readthedocs.io/>`_ :cite:`ching:17` 
and  distributed in the data exchange file format :cite:`decarlo:02` together with a python script 
to generate them (see individual phantom home page) to load and perform a basic 
reconstruction using tomoPy  :cite:`Gursoy:14a`

To reconstruct the phantom with tomopy  you may run the phantom
`Jupyter notebook <https://jupyter-notebook.readthedocs.io/en/stable/>`_
example on your local machine or run the equivalent Python
scripts from `here <https://github.com/tomography/tomobank/tree/master/docs/source/ipynb/>`_.

.. warning:: the phantoms in tomobank were generated with `XDesign VERSION 0 2 0 dev0 <https://github.com/tomography/xdesign/tree/1d67599b8f104ebded86bac98100dbf15e251a66>`_. If you want to generate the very same phantoms you should use this version (where sinogram() was defined). The xdesign version information for phantom_00001.py is saved in the HDF file under instrument_name="XDesign VERSION:0.2.0.dev0+1d67599b8f104ebded86bac98100dbf15e251a66 FUNCTION: SlantedSquares(count=16, angle=5/360*2*np.pi, gap=0.01), prop='mass_atten'" .   Please look at  `this examples <https://xdesign.readthedocs.io/en/stable/demos/FullReferenceMetrics.html#Simulate-data-acquisition>`_ to generate new phantoms using the latest xdesign version. If of interest, you are welcome to contribute new phantoms to tomobank.


.. toctree::
   
   phantom/docs.phantom.standard
   phantom/docs.phantom.wet_circles
   phantom/docs.phantom.foams
   phantom/docs.phantom.magnetic
   phantom/docs.phantom.dynamic
