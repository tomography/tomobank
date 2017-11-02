Phantoms
========

All phantom data sets are generated with `XDesign <http://myxdesign.readthedocs.io/>`_ :cite:`ching:17` 
and  distributed in the data exchange file format :cite:`decarlo:02` together with a python script 
to generate them (see individual phantom home page) and with the python script 
:download:`tomopy_rec.py <../../docs/demo/tomopy_rec.py>` to load and perform a basic 
reconstruction using tomoPy  :cite:`Gursoy:14a`.

Example: ::

    python tomopy_rec.py phantom_00001.h5

.. toctree::

   phantom/docs.phantom.standard
   phantom/docs.phantom.wet_circles
   phantom/docs.phantom.foams
..   phantom/docs.phantom.bio
