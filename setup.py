#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import sys
from io import open as io_open

__version__ = '0.0.1'
src_dir = os.path.abspath(os.path.dirname(__file__))

README_rst = ''
fndoc = os.path.join(src_dir, 'README.rst')
with io_open(fndoc, mode='r', encoding='utf-8') as fd:
    README_rst = fd.read()
setup(
    name='niftypet',
    version=__version__,
    description='CUDA-accelerated Python utilities for high-throughput PET/MR image reconstruction and analysis',
    #long_description=README_rst,
    long_description="""Currently a placeholder package which doesn't work (for now).
See https://github.com/pjmark/NiftyPET instead.""",
    license='Apache 2.0',
    url='https://niftypet.readthedocs.io',
    maintainer='Casper da Costa-Luis',
    maintainer_email='casper.dcl@physics.org',
    platforms=['any'],
    #packages=['niftypet', 'niftypet.nimpa', 'niftypet.nipet'],
    #provides=['niftypet'],
    setup_requires=['numpy'],
    install_requires=['nimpa<2', 'nipet<2'],
    python_requires='>=2.7, !=3.*',
    classifiers=[
        # Trove classifiers
        # (https://pypi.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    keywords='PET image reconstruction and analysis',
)
