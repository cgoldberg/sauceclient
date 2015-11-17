==========================
sauceclient Python package
==========================

**Python client library for Sauce Labs API.**

About sauceclient
=================

`sauceclient` is a Python client library, used for accessing the Sauce Labs
API to retrieve and update information about resources such as:

 * Information
 * Jobs
 * Provisioning
 * Usage
 * Assets (Logs, Videos, Screenshots)

`sauceclient` is *not* used for running your tests on Sauce Labs'
service.  (That is done via `Selenium WebDriver`_).

.. _Selenium WebDriver: selenium_on_sauce.html

Install
=======

 * with `pip`::

      pip install sauceclient

About Sauce Labs
================

`Sauce Labs <https://saucelabs.com>`_ is a service that allows you to run
remote Selenium WebDriver tests from their cloud. They have VM's with 100+
browser/OS combinations, allowing comprehensive cross-browser cross-platform
test coverage.

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

Related Links
=============

* `Sauce Labs <https://saucelabs.com>`_
* `Sauce Labs REST API documentation <http://saucelabs.com/docs/rest>`_
* `Python bindings for Selenium WebDriver <http://pypi.python.org/pypi/selenium>`_
