=============
Installation
=============

.. note:: 
  
  **Quick note on ways of installation**

  Assumes a compatible GPU device with installed CUDA, git and cmake (details below).

  - ``pip`` installation

    .. code-block:: none
      
      pip install --no-binary :all: --verbose nipet

    Apart from ``nipet`` itself, it will also install all relevant packages, including ``nimpa``.

  - from source using ``git`` and ``pip``/setup.py

    .. code-block:: none

      git clone https://github.com/pjmark/NIMPA.git
      git clone https://github.com/pjmark/NIPET.git

      cd ./NIMPA
      pip install --no-binary :all: --verbose -e .
      cd ../NiftyPET
      pip install --no-binary :all: --verbose -e .


    This will install \"editable\" distribution at the source locations for both, ``nimpa`` and ``nipet``.  This way the packages can be modified and/or updated using ``git pull``.  The detailed steps for installation are given below.








*NiftyPET* is a `Python name space package <https://packaging.python.org/guides/packaging-namespace-packages>`_, encompassing the two packages: ``nimpa`` and ``nipet``. Currently, the packages are available for Python 2.7 in Linux and Windows systems. So far, it has been deployed and tested on CentOS 6.8 and 7, Ubuntu 14.04, 16.04 and 18.04 as well as Windows 10 (limited), all accompanied with Python 2.7 distribution from Anaconda while using Python C extensions for the core CUDA routines.  Linux systems are recommended due to their robustness and stability and the support for Windows is very limited.


Dependencies
------------

Hardware
^^^^^^^^

* **GPU device**: Supported are GPU devices from NVIDIA with the compute capability of at least 3.5 (e.g., NVIDIA Tesla K20/40).  It is recommended to have at least 5 GB of GPU memory.  *NiftyPET* supports multiple CUDA devices and so far, the following devices have been tested with *NiftyPET*: 

   * NVIDIA Tesla K20/40,
   * NVIDIA Titan Xp,
   * NVIDIA GeForce GTX 1060,
   * NVIDIA GeForce GTX 1080.
   
* **CPU host**: The GPU device can be accessed by a CPU host, with a reasonable computing power for some other image processing routines (e.g., image registration, etc.).  It is recommended to have at least 16 GB of RAM, although we have managed to run dynamic reconstruction using old PC workstations with as little as 11 GB of RAM.


Software
^^^^^^^^

*NitfyPET* installation needs pre-installed the following software:

* **C/C++ compiler**: **GCC** is used in Linux systems, while for Windows Visual Studio is used (see below for Windows installation).

  On Linux systems it can be installed as follows:

  * Ubuntu: 

    .. code-block:: none

      apt-get install build-essential

  
  * CentOS: 

    .. code-block:: none

      yum group install "Development Tools"


*  **CUDA toolkit**: a parallel computing platform and programming model, which includes CUDA compiler (NVCC) and runtime API.  The latest CUDA toolkit can be obtained for free from https://developer.nvidia.com/cuda-downloads.  For any specific operating system follow the CUDA installation guide at https://docs.nvidia.com/cuda/index.html.  

  .. tip::

    In CentOS, it is necessary to install DKMS (Dynamic Kernel Module Support), which can be obtained from https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm. Then, it can be installed as follows:
   
    .. code-block:: none

      rpm -ivh epel-release-latest-7.noarch.rpm
      yum -y install dkms


  Make sure that CUDA is installed with appropriate paths to CUDA resources setup, that is, for CUDA 10.0 on Linux systems, it is:
   
  .. code-block:: none

    export PATH=/usr/local/cuda-10.0/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH

  This can be added to ``.profile`` or ``.bashrc`` file in your home directory (Linux). For more details see http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions.


* **Git**: a version control system, used for downloading *NiftyPET* and other necessary tools, i.e.: ``NiftyReg`` and ``dcm2niix``. For more details on installing ``git`` see https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

  On Linux systems it can be installed as follows:

  * Ubuntu:

    .. code-block:: none

      apt-get install git

  * CentOS:

    .. code-block:: none
   
      yum install git

* **cmake**: a tool for cross-platform software package building, which can be downloaded freely from https://cmake.org/install/. For the Ubuntu distribution, cmake together with the user GUI can be installed as follows:

  .. code-block:: none

    sudo apt-get update
    sudo apt-get install cmake cmake-curses-gui

  .. tip::

    For CentOS, it is recommended to install ``cmake`` from source from the above website for the latest version (version 3).  Binary and source distributions are provided.


* **Python 2.7**: a free high-level programming language, through which all the GPU routines are available for the user.
  The easiest way to run *NiftyPET* in Python is by using the Anaconda distribution which includes ``Jupyter Notebook``.  To download Anaconda visit https://www.anaconda.com/download/ and choose Python 2.7.

* **Required Python packages**: If another distribution of Python is used, make sure that the following standard Python packages are installed: ``scipy``, ``numpy``, ``matplotlib``, ``math`` (these are supplied by default in the Anaconda distribution).

  * **Specialised Python packages**: the following packages for medical image I/O and manipulation are automatically installed during NiftyPET installation (not distributed by default):

    * ``nibabel``: http://nipy.org/nibabel/
    * ``pydicom``: http://pydicom.readthedocs.io/en/stable/getting_started.html#installing

    If for whatever reason the automatic installation fails, the two packages can be installed together as follows:

    .. code-block:: none

      conda install -c conda-forge nibabel
      conda install -c conda-forge pydicom


.. _niftypet-install:

*NiftyPET* installation
-----------------------



Using ``pip``
^^^^^^^^^^^^^

* NiftyPET:``nimpa``


  To install ``nimpa`` with CUDA source compilation for the given CUDA version and operating system (Linux is preferred), simply type:

  .. code-block:: none

    pip install --no-binary :all: --verbose nimpa


* NiftyPET:``nipet``


  To install ``nipet``, the core of NiftyPET image reconstruction, type:

  .. code-block:: none

    pip install --no-binary :all: --verbose nipet


  This will also install ``nimpa`` if it is not yet installed and will compile the CUDA C source code for the user's Linux system and CUDA version (>=7.0).




From source using ``git`` and ``pip``/``setup.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The source code of full version of ``nimpa`` and ``nipet`` packages can be downloaded to a specific folder using ``git`` as follows:

::

  git clone https://github.com/pjmark/NIMPA.git
  git clone https://github.com/pjmark/NIPET.git

Alternatively, it can also be downloaded with an `SSH` key pair setup:

::

  git clone git@github.com:pjmark/NIMPA.git
  git clone git@github.com:pjmark/NIPET.git

After a successful download, navigate to folder ``nimpa`` and run inside one of the folder the following:

::

  1) python setup.py install
  2) pip install --no-binary :all: --verbose .
  3) pip install --no-binary :all: --verbose -e .

The last option with the ``-e`` makes the installation \"editable\", alowing the user to modify the source code themselves or by pulling newer versions from ``git`` using ``git pull``.

Identically for ``nipet``, run one of the following:

::

  1) python setup.py install
  2) pip install --no-binary :all: --verbose . 
  3) pip install --no-binary :all: --verbose -e .


The installation will call on ``cmake``, which will run automatically and generate make files, and then run ``make`` to build all the CUDA C routines and Python C extensions.  Following this, the compiled Python modules will be installed into the specific Python package location.



Third party software installed with *NiftyPET* 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The installation *NiftyPET* will automatically install additional third party software, used for extra capabilities, such as image registration and conversion.  *NiftyReg* and *dcm2niix* will be installed in ``NiftyPET_tools`` folder, in your home directory:

* **dcm2niix**: conversion of DICOM images to NIfTI images (v1.0.20171204).  If for some reason the automatic installation fails (e.g., due to a problem with dependencies), try to download the source code from https://github.com/rordenlab/dcm2niix and compile it, or use the pre-complied version with current release available at https://github.com/rordenlab/dcm2niix/releases/.

* **NiftyReg**: image registration and resampling tool.  The stable version (16 Nov 2017) is fetched and installed automatically using

  ::

    git clone https://github.com/KCL-BMEIS/niftyreg/

  Some details for a manual install can be found at http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg_install (can be outdated).



Installation in Conda environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the advantages of using ``conda`` (part of Anacoda) and Python is the possibility of having separate environments for different versions of Python and/or packages installed in them.  Thus, ``conda`` environments enable the user to set up *NiftyPET* differently for various applications (e.g., different image resolution, radio-pharmaceutical-optimised attenuation and/or scatter correction, etc.). Below is demonstrated an installation of NiftyPET into environment called `niftypet`.

Create environment called, for example, `niftypet`, by running this command:

::

  conda create --name niftypet

Activate the conda environment in Linux:

::

  source activate niftypet

in Windows:

::

  activate niftypet

It may be necessary to install additional required packages, like the following:

::

  conda install -c anaconda pycurl 
  conda install -c anaconda matplotlib
  conda install -c anaconda ipython
  conda install -c conda-forge nibabel
  conda install -c conda-forge pydicom


*NiftyPET* can now be installed as described above in :ref:`niftypet-install`, while making sure that the ``conda`` environment is active.  Please note, that for some reason it may be necessary to deactivate the conda environment and then active it again (and close the terminal) so that the `NiftyPET` package will be recognised in the specific path of the Python environment, and be thus importable (``import nipet``).


Post-installation checks
------------------------

Default CUDA device
^^^^^^^^^^^^^^^^^^^

The default CUDA device used for GPU calculations is chosen during the installation together with the CUDA architecture code compilation, which is specific for a given GPU device with a specific compute capability.  This information is stored in ``resources.py`` in ~/.niftypet/ folder, created during the installation (additional folder may be present corresponding to the ``conda`` environment).  For example, for the NVIDIA Titan Xp with compute capability of 6.1, it will look like this:

::

  # DO NOT MODIFY BELOW--DONE AUTOMATICALLY
  ### start GPU properties ###
  DEV_ID = 0
  CC_ARCH = '-gencode=arch=compute_61,code=compute_61;'
  ### stop GPU properties ###

Any available (installed) CUDA devices can be chosen within Python for any image reconstruction or part of the reconstruction pipeline.

Paths for the third-party software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If for some reason, the paths to the tools for image registration, resampling and conversion (DICOM -> NIfTI) are found incorrect, it can be checked by viewing ``resources.py`` file in ``~/.niftypet`` folder in Linux (for ``conda`` environment there will be an additional folder with the name of the environment, which contains ``resources.py``, specific for the environment).  In Windows, it is located in the local application data folder.   It is recommended that the paths and device properties are not manually edited, but are changed rather by rerunning the installation.

::
  
  # paths to apps and tools needed by NiftyPET
  ### start NiftyPET tools ###
  PATHTOOLS = '/path/to/NiftyPET_tools/'
  RESPATH = '/path/to/NiftyPET_tools/niftyreg/bin/reg_resample'
  REGPATH = '/path/to/NiftyPET_tools/niftyreg/bin/reg_aladin'
  DCM2NIIX = '/path/to/NiftyPET_tools/dcm2niix/bin/dcm2niix'
  HMUDIR = '/path/to/mmr_hardware_mumaps'
  ### end NiftyPET tools ###

Note that the hardware :math:`\mu`-maps are not distributed with this software, and have to be obtained from the Siemens Biograph mMR scanner.



Jupyter Notebook
----------------

Jupyter Notebook is a wonderful tool, useful for sharing and replicating image reconstruction methods written in Python.  It allows introspection, plotting and sharing of any intermediate results (e.g., sinograms and images generated during the  reconstruction pipeline) or any end result.  For this reason, it is best when Python and iPython are installed through Anaconda, which by default includes Jupyter Notebook.  See http://jupyter.readthedocs.io/en/latest/tryjupyter.html for more details and http://jupyter.readthedocs.io/en/latest/install.html for a manual installation.

