===========================================
sauceclient Python package -- documentation
===========================================

**Python client library for Sauce Labs API.**

About sauceclient
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

Install
=======

 * with `pip`::
 
      pip install sauceclient

 or:

 * download the latest `sauceclient` `Package <http://pypi.python.org/pypi/sauceclient#downloads>`_ (souce tarball)
   from `PyPI <http://pypi.python.org/pypi>`_, unarchive, and run::

     python setup.py install

About Sauce Labs
================

`Sauce Labs <https://saucelabs.com>`_ is a service that allows you to run
remote Selenium WebDriver tests from their cloud. They have VM's with 100+
browser/OS combinations, allowing comprehensive cross-browser cross-platform
test coverage. Sauce Labs is a paid service, offerning various 
`usage plans <https://saucelabs.com/pricing>`_. They offer 
`free accounts <https://saucelabs.com/signup/plan/free>`_ for limited/trial
use. `Open Sauce <https://saucelabs.com/signup/plan/OSS>`_ accounts are also
free.  Open Sauce allows unlimited automated code minutes, and 3 parrallel 
VM's (simultaneous tests), if you have a verified Open Source project.

Example sauceclient Usage
=========================

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

Running Selenium WebDriver
==========================

.. toctree::
    :maxdepth: 4
    
    selenium_on_sauce
    
Development
===========

.. toctree::
    :maxdepth: 4

    development

Related Links
=============

* `Sauce Labs <https://saucelabs.com>`_
* `Sauce Labs REST API documentation <http://saucelabs.com/docs/rest>`_
* `Python bindings for Selenium WebDriver <http://pypi.python.org/pypi/selenium>`_
