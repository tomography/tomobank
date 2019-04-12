Dagstuhl Seminar 19151 
======================

This repository contains a series of datasets representing the four challanges as discussed at the Dagstuhl Seminar 19151 on
Visual Computing in Material Science | April 7-12, 2019

You can upload a data set `here <https://app.globus.org/file-manager?origin_id=e133a81a-6d04-11e5-ba46-22000b92c6ec&origin_path=%2Fupload%2Fdagstuhl_2019%2F>`_.

To upload data from your computer to TomoBank you need to install 
`Globus Endpoint Personal <https://www.globus.org/globus-connect-personal>`_.

All tomobank data sets are distributed in the native file format or in data exchange :cite:`decarlo:02` together 
with the python script :download:`tomopy_rec.py <../../docs/demo/tomopy_rec.py>`
to load and perform a basic reconstruction using tomoPy  :cite:`Gursoy:14a`.

Usage: ::

    python tomopy_rec.py -h
	usage: tomopy_rec.py [-h] [--axis [AXIS]] [--type [TYPE]] [--nsino [NSINO]]
                     fname

	positional arguments:
  		fname            file name of a tmographic dataset: /data/sample.h5

	optional arguments:
  		-h, --help       show this help message and exit
  		--axis [AXIS]    rotation axis location: 1024.0 (default 1024.0)
  		--type [TYPE]    reconstruction type: full (default slice)
  		--nsino [NSINO]  location of the sinogram used by slice reconstruction (0
                   		 top, 1 bottom): 0.5 (default 0.5)

Example: ::

    python tomopy_rec.py /tomobank/tomo_00001.h5 --axis 1024

