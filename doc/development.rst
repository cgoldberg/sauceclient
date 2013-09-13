=======================
sauceclient Development
=======================

Requirements
============

 * Python 2.7
 * git

Source Code Repository (GitHub)
===============================

 * `sauceclient` on `GitHub <https://github.com/cgoldberg/sauceclient>`_

Getting the Code
================

Source code is stored in a git repository and can be retrieved with
``git`` using various protocols.

Clone the Repository:

 * SSH::

    $ git clone git@github.com:cgoldberg/sauceclient.git

 * HTTPS::

    $ git clone https://github.com/cgoldberg/sauceclient.git


Install package in development mode
===================================

 * clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git
    $ cd sauceclient

 * install `sauceclient` in development mode::

    $ python setup.py develop

Now, you can make changes directly to the source files in the original location
where you cloned the git repository, and those changes will be reflected
immediately when you use `sauceclient` in your Python scripts. See
`Development Mode`_ in the `setuptools` documentation for more details.

.. _Development Mode:  http://peak.telecommunity.com/DevCenter/setuptools#development-mode


Running the Unit Tests
======================

 * clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git
    $ cd sauceclient

 * edit ``test_sauceclient.py``, and change the
   test parameters to match your Sauce Labs account info::

    SAUCE_USERNAME = 'your-username-string'
    SAUCE_ACCESS_KEY = 'your-access-key-string'
    TEST_JOB_ID = 'a-valid-test-job-id'

 * run tests by executing ``test_sauceclient.py``, or using ``unittest`` discovery::

    $ python -m unittest discover

Generating the Documentation
============================

 * requires: `python-sphinx <http://sphinx-doc.org>`_
 * build the docs locally::

     $ git clone git@github.com:cgoldberg/sauceclient.git
     $ cd sauceclient
     $ sphinx-build -b html doc html_docs

 * generated results end up in ``./html_docs/``
