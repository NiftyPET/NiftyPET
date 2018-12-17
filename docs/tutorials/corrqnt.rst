================================
Corrections for quantitative PET
================================


Decay correction
----------------

During any PET acquisition, the radio-tracer activity, :math:`A_t`, decays according to:

.. math::

   A_t = A_0e^{-\lambda t},

where :math:`A_0` is the reference activity at time :math:`t_0`. The decay constant :math:`\lambda` is defined as:

.. math::

   \lambda = \frac{\ln(2)}{T_{1/2}},

where :math:`T_{1/2}` is the half-life of the radionuclide.

Likewise, for activity :math:`A_t` at time :math:`t`, the original activity is simply:

.. math::

   A_0 = A_te^{\lambda t}.

Therefore, the decay correction :math:`C_{\textrm{decay}}^{t_0}` with reference to :math:`t_0` is:

.. math::
   
   C_{\textrm{decay}}^{t_0} = \frac{\lambda e^{\lambda t_0} (t-t_0) }{1-e^{-\lambda (t-t_0)}}.
   
See also http://www.turkupetcentre.net/petanalysis/decay.html.

The decay correction is applied automatically with the reference to the beginning of the image time frame.  It is controlled by the dictionary entry ``Cnt['DCYCRR']``.  For example, if the scanner is initialised as follows:

.. code-block:: python

  import numpy as np
  import sys, os

  # NiftyPET image reconstruction package (nipet)
  from niftypet import nipet
  # NiftyPET image manipulation and analysis (nimpa)
  from niftypet import nimpa

  # get all the Biograph mMR parameters
  mMRpars = nipet.get_mmrparams()


Then the default decay correction can be switched off, if the following line:

.. code-block:: python
   
   mMRpars['Cnt']['DCYCRR'] = False,
   
is placed before image reconstruction.  By default ``mMRpars['Cnt']['DCYCRR'] = True``.
