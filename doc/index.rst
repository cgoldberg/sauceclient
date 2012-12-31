===========================================
sauceclient Python package -- documentation
===========================================

**Python client library for Sauce Labs API.**

* Development:

 * `sauceclient` on `GitHub <https://github.com/cgoldberg/sauceclient>`_

* Install (coming soon):

 * with `pip`::
 
    pip install sauceclient

 or:

 * download `Package <http://pypi.python.org/pypi/sauceclient#downloads>`_ (souce tarball)
   from `PyPI <http://pypi.python.org/pypi>`_, unarchive, and run::

    python setup.py install

about Sauce Labs
================


about sauceclient
=================

`sauceclient` is a Python client library, used for accessing the Sauce Labs
API to retrieve and update information about resources such as:

 * Information
 * Jobs
 * Provisioning
 * Usage

`sauceclient` is *not* used for running your tests on Sauce Labs'
service.  (That is done via `Selenium WebDriver`_).

.. _Selenium WebDriver: selenium_on_sauce.html

example usage
=============

* public access::

    import sauceclient
    
    sc = sauceclient.SauceClient()
    status = sc.information.get_status()
    
* with authorization::

    import sauceclient
    
    sc = sauceclient.SauceClient(
        'sauce-username',
        'sauce-access-key',
    )
    job_ids = sc.jobs.get_job_ids()

Python Module Reference
=======================

.. toctree::
    :maxdepth: 4
    
    sauceclient
    test_sauceclient

Prerequisite Reading
====================

.. toctree::
    :maxdepth: 4
    
    selenium_on_sauce
    development
    
Related Links
=============

* `Sauce Labs <https://saucelabs.com>`_
* `Sauce Labs REST API documentation <http://saucelabs.com/docs/rest>`_
* `Python bindings for Selenium WebDriver <http://pypi.python.org/pypi/selenium>`_
