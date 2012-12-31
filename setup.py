#!/usr/bin/env python


""" setup/install script for sauceclient. """


import os
from distutils.core import setup

import sauceclient


this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.rst')) as f:
    LONG_DESCRIPTION = '\n' + f.read()


setup(
    name='sauceclient',
    version=sauceclient.__version__,
    packages=['sauceclient'],
    author='Corey Goldberg',
    author_email='cgoldberg _at_ gmail.com',
    description='Python client library for Sauce Labs API.',
    long_description=LONG_DESCRIPTION,
    url='http://cgoldberg.github.com/sauceclient/',
    download_url='http://pypi.python.org/pypi/sauceclient',
    keywords='saucelabs selenium testing'.split(),
    license='Apache v2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ]
)
