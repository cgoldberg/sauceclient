=======================
sauceclient Development
=======================

Requirements
============

 * Python 2.7 or 3.x
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


Running the Unit Tests
======================

 * clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git
    $ cd sauceclient

 * set the following environment variables::

    $ export SAUCE_USERNAME='your-username-string'
    $ export SAUCE_ACCESS_KEY='your-access-key-string'
    $ export TEST_JOB_ID='a-valid-test-job-id'

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
