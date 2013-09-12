#!/usr/bin/env python
#
#   Copyright (c) 2013 Corey Goldberg
#
#   This file is part of: sauceclient
#   https://github.com/cgoldberg/sauceclient
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#


"""setup/install script for sauceclient."""


import os
from setuptools import setup

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.rst')) as f:
    LONG_DESCRIPTION = '\n' + f.read()


from sauceclient import __version__


setup(
    name='sauceclient',
    version=__version__,
    py_modules=['sauceclient'],
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ]
)
