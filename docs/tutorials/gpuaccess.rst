
==================================
Accessing and querying GPU devices
==================================

`IPython <https://ipython.readthedocs.io/en/stable/index.html>`_ is an interactive Python prompt, particularly useful for PET/MR imaging.  Start IPython by issuing ``ipython`` in the terminal to obtain the following::

  Python 2.7.15 |Anaconda custom (64-bit)| (default, May  1 2018, 23:32:55) 
  Type "copyright", "credits" or "license" for more information.

  IPython 5.7.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.

  In [1]: 

.. note:: At this stage Python 2.7 is supported.  Support for Python 3 is coming soon.



Import ``nimpa`` package from Python *NiftyPET* namespace and run the :

.. code-block:: python

  from niftypet import nimpa
  nimpa.gpuinfo()

which for two NVIDIA GPU devices used for this documentation (TITAN Xp and Quadro K4200) will produce::

  In [1]: from niftypet import nimpa
    ...:  nimpa.gpuinfo()
    ...: 
  Out[1]: [('TITAN X (Pascal)', 12788L, 6L, 1L), ('Quadro K4200', 4231L, 3L, 0L)]

  In [2]: 

Please note that only the first device is supported, i.e., the compute capability is ``>=3.5``::

  In [3]: nimpa.gpuinfo()[0][2:]
  Out[3]: (6L, 1L)


The same fuction is available in ``nipet``, i.e.:

.. code-block:: python

  from niftypet import nipet
  nipet.gpuinfo()


It's also possible to get extended information about the installed GPU devices by running either

.. code-block:: python

  nipet.gpuinfo(extended=True)

or

.. code-block:: python

  nimpa.gpuinfo(extended=True)


For the above GPU devices, the following will be obtained::
  
  In [4]: nimpa.gpuinfo(extended=True)
  i> there are 2 GPU devices.

  ----------------------------------------
  CUDA device: TITAN X (Pascal), ID = 0
  ----------------------------------------
  i> total memory [MB]:12788.50
  i> shared memory/block [kB]:   49.15
  i> registers (32bit)/thread block: 65536
  i> warp size: 32
  i> compute capability: 6.1
  i> clock rate [MHz]: 1531.00
  i> ECC enabled? 0
  i> max # threads/block: 1024

  i> Memory available: 12788.50[MB]
     Used: 504.37[MB] 
     Free:12284.13[MB]


  ----------------------------------------
  CUDA device: Quadro K4200, ID = 1
  ----------------------------------------
  i> total memory [MB]:4231.99
  i> shared memory/block [kB]:   49.15
  i> registers (32bit)/thread block: 65536
  i> warp size: 32
  i> compute capability: 3.0
  i> clock rate [MHz]:  784.00
  i> ECC enabled? 0
  i> max # threads/block: 1024

  i> Memory available: 4231.99[MB]
     Used:1117.06[MB] 
     Free:3114.93[MB]

  [('TITAN X (Pascal)', 12788L, 6L, 1L), ('Quadro K4200', 4231L, 3L, 0L)]
  Out[4]: [('TITAN X (Pascal)', 12788L, 6L, 1L), ('Quadro K4200', 4231L, 3L, 0L)]