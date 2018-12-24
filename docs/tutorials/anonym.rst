===================
DICOM anonymisation
===================

`DICOM <https://en.wikipedia.org/wiki/DICOM>`_ data `anonymisation <https://en.wikipedia.org/wiki/Data_anonymization>`_ or `pseudonymisation <https://en.wikipedia.org/wiki/Pseudonymization>`_ is a process of removing sensitive personal information from DICOM attributes .  This ensures compliance with the EU's General Data Protection Regulation (`GDPR <https://eugdpr.org/>`_); so that the people who are imaged remain anonymous when their image data is distributed for wider scientific or clinical research.

The difference between anonymisation and pseudonymisation is that the former does not allow re-identification, while the latter does.  In pseudonymisation the personally identifiable information is replaced with artificial identifiers, which must be kept separately and safely.  Importantly, however, it has to be recognised that with current machine learning techniques, absolute protection of digital imaging data is almost impossible.  For example, in an MR study of the head, effective anonymisation would also need to involve  irreversible image deformation of the face :cite:`EuropeanSocietyofRadiologyESR2017`.

---------------------------
Anonymisation in *NiftyPET*
---------------------------

The anonymisation can be achieved using function ``dcmanonym`` in sub-package ``nimpa``.  For example, sensitive information, such as the patient's name, date of birth, etc., can be checked and displayed by:   

.. code-block:: python

   from niftypet import nimpa
   dcmpath = '/path/to/DICOM-file'
   nimpa.dcmanonym(dcmpath, displayonly=True)

If it needs anonymisation or pseudonymisation, the sensitive information, such as the patient's name, date of birth (``dob``) and physician's name, has to be replaced by the user-defined strings, i.e.:

.. code-block:: python

   nimpa.dcmanonym(dcmpath,
                   patient='Anonymous',
                   physician='DR. Anonymous',
                   dob='19000101',
                   verbose=True)

The argument ``dcmpath`` in the above call, can be not only the path (a Python string) to a single DICOM file, but also it can be a Python list of DICOM file paths, the path to a folder containing DICOM files, or a dictionary ``datain`` containing all the data (including raw data) needed for a standalone image reconstruction.  For example, assuming that the scanner (here the Biograph mMR) is initialised and the path to raw data is provided, i.e.:

.. code-block:: python

   from niftypet import nipet
   from niftypet import nimpa

   # get all the scanner parameters
   mMRparams = nipet.get_mmrparams()
   folderin = '/path/to/raw-data'

   # automatically categorise the input data
   datain = nipet.classify_input(folderin, mMRparams)

then all the DICOM data required for reconstruction can be anonymised simply by:

.. code-block:: python

   nimpa.dcmanonym(datain,
                   patient='RandomID',
                   physician='Dr. Hopefully Nice',
                   dob='19800101',
                   verbose=True)

Please note, that the anonymisation of the Biograph mMR data goes somewhat deeper than just modifying the DICOM attributes---it also extracts the specific CSA headers and searches them for the patient's name.