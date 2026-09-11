Grapevine Petiole
-----------------

Dehydration Sequence
~~~~~~~~~~~~~~~~~~~~

The Grapevine Petiole Dehydration datasets contain micro-tomography (microCT) data measuring embolisms in xylem vessels during dynamic *in-situ* dehydration, along with expert-curated ground truth semantic segmentation masks.

The datasets were acquired at the Advanced Light Source (ALS) beamline 8.3.2 in parallel beam geometry. The experimental conditions are reported in the table below:

+---------------------------------+------------------------------------+
| Instrument                      |        ALS beamline 8.3.2          |
+---------------------------------+------------------------------------+
| Energy                          |        23 keV                      |
+---------------------------------+------------------------------------+
| Monochromator                   |        Double Multilayer           | 
+---------------------------------+------------------------------------+
| Scan Range                      |        180 degree                  |
+---------------------------------+------------------------------------+
| Mode                            |        Continuous Tomo             |
+---------------------------------+------------------------------------+
| Sample Detector Distance        |        129.9 mm                    |
+---------------------------------+------------------------------------+
| Detector Name                   |        pcoEdge                     |
+---------------------------------+------------------------------------+
| Pixel Size                      |        0.635 µm                    |
+---------------------------------+------------------------------------+
| Objective Magnification         |        Optique 10x                 |
+---------------------------------+------------------------------------+
| Scintillator                    |        50 um LuAG                  |
+---------------------------------+------------------------------------+

The dataset includes 14 raw tomographic scans divided into two dynamic dehydration sequences, along with a unified archive of high-quality expert-curated segmentation masks:

*   **Expert-curated Masks**: :download:`annotations.tar.zst <https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fannotations.tar.zst>` - Semantic instances for 42 cross-sections (background, cortex, phloem fibers, phloem, hydrated xylem, air-filled pith, water-filled pith, dehydrated xylem, and ignore regions).
*   **Time Series 1**: 6 sequential scans of a single grapevine petiole undergoing dehydration (Petioles 22-27).
*   **Time Series 2**: 8 sequential scans of a second grapevine petiole undergoing dehydration (Petioles 33-40).

To load the datasets and perform a basic reconstruction using `tomopy <https://tomopy.readthedocs.io>`_ ::

    tomopy recon --file-name 20260221_140347_petiole23.h5 --rotation-axis 1280

.. |grapevine| image:: ../img/tomo_grapevine.png
    :width: 20pt
    :height: 20pt

+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| Tomo ID               | Sequence | Sample / Filename                               | Image Preview  | Reconstruction   |
+=======================+==========+=================================================+================+==================+
| petiole_22_           | TS1      | 20260221_135217_petiole22.h5                    | |grapevine|    | rec_22_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_23_           | TS1      | 20260221_140347_petiole23.h5                    | |grapevine|    | rec_23_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_24_           | TS1      | 20260221_140816_petiole24.h5                    | |grapevine|    | rec_24_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_25_           | TS1      | 20260221_141434_petiole25.h5                    | |grapevine|    | rec_25_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_26_           | TS1      | 20260221_141945_petiole26.h5                    | |grapevine|    | rec_26_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_27_           | TS1      | 20260221_142453_petiole27.h5                    | |grapevine|    | rec_27_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_33_           | TS2      | 20260221_154210_petiole33.h5                    | |grapevine|    | rec_33_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_34_           | TS2      | 20260221_154714_petiole34.h5                    | |grapevine|    | rec_34_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_35_           | TS2      | 20260221_155149_petiole35.h5                    | |grapevine|    | rec_35_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_36_           | TS2      | 20260221_155821_petiole36.h5                    | |grapevine|    | rec_36_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_37_           | TS2      | 20260221_160336_petiole37.h5                    | |grapevine|    | rec_37_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_38_           | TS2      | 20260221_160807_petiole38.h5                    | |grapevine|    | rec_38_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_39_           | TS2      | 20260221_161542_petiole39.h5                    | |grapevine|    | rec_39_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+
| petiole_40_           | TS2      | 20260221_162040_petiole40.h5                    | |grapevine|    | rec_40_          |
+-----------------------+----------+-------------------------------------------------+----------------+------------------+

.. _petiole_22: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_135217_petiole22.h5
.. _petiole_23: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_140347_petiole23.h5
.. _petiole_24: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_140816_petiole24.h5
.. _petiole_25: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_141434_petiole25.h5
.. _petiole_26: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_141945_petiole26.h5
.. _petiole_27: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_142453_petiole27.h5
.. _petiole_33: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_154210_petiole33.h5
.. _petiole_34: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_154714_petiole34.h5
.. _petiole_35: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_155149_petiole35.h5
.. _petiole_36: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_155821_petiole36.h5
.. _petiole_37: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_160336_petiole37.h5
.. _petiole_38: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_160807_petiole38.h5
.. _petiole_39: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_161542_petiole39.h5
.. _petiole_40: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Fraw%2F20260221_162040_petiole40.h5
.. _rec_22: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole22%2F
.. _rec_23: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole23%2F
.. _rec_24: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole24%2F
.. _rec_25: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole25%2F
.. _rec_26: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole26%2F
.. _rec_27: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole27%2F
.. _rec_33: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole33%2F
.. _rec_34: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole34%2F
.. _rec_35: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole35%2F
.. _rec_36: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole36%2F
.. _rec_37: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole37%2F
.. _rec_38: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole38%2F
.. _rec_39: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole39%2F
.. _rec_40: https://app.globus.org/file-manager?destination_id=472d6c6f-dc53-420f-9a12-b3515282f1c1&destination_path=%2Ftomobank_petioles%2Freconstruction%2Fpetiole40%2F
