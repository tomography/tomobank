XANES
-----

SSRL XANES tomography
~~~~~~~~~~~~~~~~~~~~~

This spectro-tomography dataset contains 67 tomograms of an NMC battery cathode particle at different x-ray energies. For each tomogram, 180 projection images were acquired at different angles. The x-ray energy points were selected such that we will be able to reconstruct the elemental maps of Mn, Co, and Ni (6 energies, one above and one below the respective K-edges of Mn, Co, and Ni), and a XANES scan across the Ni K-edge (for valence state distribution). The idea is to correlate the compositional heterogeneity with the redox heterogeneity.  To read the data use :download:`read_xrm_script.py <../../demo/read_xrm_script.py>` python script.

There are two independent image alignment tasks: 1) we need to correct the image jitter in a tomography dataset and 2) we need to register the tomograms at different x-ray energies.

For task 1, the SSRL team uses an iterative alignment protocol described in :cite:`Yu:fv5093`, which works fine except that this process is very slow.

For task 2, the SSRL team use TXM-Wizard to register the projection images in the same sample orientation angle by angle. Images at different x-ray energies are of different magnification and contrast. SSRL’s approach is essentially calling the function described in section 3 of :cite:`Liu:hf5192` multiple times. An improved approach with better quality control and assessment is highly desirable. Note that the pixel size is nearly proportional to the x-ray energy.

.. |00089| image:: ../img/tomo_00089.png
    :width: 20pt
    :height: 20pt

.. _tomo_00089: https://app.globus.org/file-manager?origin_id=9f00a780-4aee-42a7-b7f4-6a2773c8da30&origin_path=%2Ftomo_00089%2F



 
+-----------------------------------------+----------------------------------------------------+
|             tomo_ID                     | 00089                                              |  
+=========================================+====================================================+
|             Image preview               | |00089|                                            |  
+-----------------------------------------+----------------------------------------------------+
|             Download                    | tomo_00089_                                        |  
+-----------------------------------------+----------------------------------------------------+
|             Instrument                  | SSRL nano-CT                                       |  
+-----------------------------------------+----------------------------------------------------+
|             Sample name                 | Heterogeneous_NMC                                  |  
+-----------------------------------------+----------------------------------------------------+
|             X-ray energy                | 6534, 6558, 7704, 7728, 8178, 8570 eV              |  
+-----------------------------------------+----------------------------------------------------+
|             Pixel size                  | 33.4 nm at 8670 eV                                 |  
+-----------------------------------------+----------------------------------------------------+
