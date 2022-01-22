=====
Usage 
=====

TomoBank data sets and phantoms are distributed using a 
`Globus <https://app.globus.org/file-manager?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Ftomobank%2F>`_ server.
The first time you use tomoBank you need to create a `Globus Account <https://docs.globus.org/how-to/get-started/>`_ 
and set up you computer as a `Globus EndPoint <https://www.globus.org/globus-connect-personal>`_.

To read tomoBank files and perform a basic tomographic reconstruction first, you must have `Conda <https://docs.conda.io/en/latest/miniconda.html>`_ installed. Next, install `tomoPy  <https://tomopy.readthedocs.io/en/latest/>`_ and all its runtime dependencies into a new Conda
environment called ``tomopy`` by running::

    $ conda create --name tomopy --channel conda-forge tomopy

Use this TomoPy installation by activating this environment::

    $ conda activate tomopy

then install `dxchange <https://dxchange.readthedocs.io/>`_::

	$ conda install -c conda-forge dxchange

and `tomopy cli <https://tomopycli.readthedocs.io/>`_::

    $ git clone https://github.com/tomography/tomopy-cli.git
    $ cd tomopy-cli
    $ python setup.py install

After the above installation all tomobank datasets and phantoms can be reconstructed with::

    $ tomopy recon --file-name tomo_0001.h5 --rotation-axis 1024.0