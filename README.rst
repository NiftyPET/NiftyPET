===========================================================
NiftyPET: High-throughput image reconstruction and analysis
===========================================================

*NiftyPET* is a Python software platform, offering high-throughput PET image reconstruction (``nipet`` -- a core package of NiftyPET: https://github.com/pjmark/NIPET) as well as image manipulation, processing and analysis (``nimpa``: https://github.com/pjmark/NIMPA) for PET/MR imaging with high quantitative accuracy and precision. The software is written in CUDA C and embedded in Python C extensions.

The scientific aspects of this software are covered in two open-access publications:

* *NiftyPET: a High-throughput Software Platform for High Quantitative Accuracy and Precision PET Imaging and Analysis* Neuroinformatics (2018) 16:95. https://doi.org/10.1007/s12021-017-9352-y

* *Rapid processing of PET list-mode data for efficient uncertainty estimation and data analysis* Physics in Medicine & Biology (2016). https://doi.org/10.1088/0031-9155/61/13/N322

Although, *NiftyPET* is dedicated to high-throughput image reconstruction and analysis of brain images, it can also be used for whole body imaging.  Strong emphasis is put on the data, which are acquired using positron emission tomography (PET) and magnetic resonance (MR), especially using the hybrid and simultaneous PET/MR scanners.  

This software platform covers the entire processing pipeline, from the raw list-mode (LM) PET data through to the final image statistic of interest (e.g., regional SUV), including LM bootstrapping and multiple reconstructions to facilitate voxel-wise estimation of uncertainties.


Author: Pawel J. Markiewicz @ University College London

Copyright 2018