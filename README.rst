==========================
sauceclient Python package
==========================

**Python client library for Sauce Labs API.**

.. image:: https://travis-ci.org/cgoldberg/sauceclient.svg?branch=master
    :target: https://travis-ci.org/cgoldberg/sauceclient

About sauceclient
=================

*sauceclient* is a Python client library for the Sauce Labs
API.

Management Options:

 * Account
 * Platform Information
 * JavaScript Unit Tests
 * Jobs & Assets (Logs, Videos, Screenshots)
 * Temporary Storage
 * Tunnels

*sauceclient* is *not* used for running your tests on Sauce Labs' service.
(That is done via `Selenium WebDriver`_).

.. _Selenium WebDriver: selenium_on_sauce.html

Install
=======

 * with `pip`::

      pip install sauceclient

About Sauce Labs
================

`Sauce Labs <https://saucelabs.com>`_ is a service for running remote Selenium
WebDriver tests. They have VM's with 800+ browser/OS combinations, allowing
comprehensive cross-browser cross-platform test coverage.

Example Usage
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
    jobs = sc.jobs.get_jobs(full=True, limit=5)

Compatibility Note
==================

Due to changes in the SauceLabs REST API, some of sauceclient's
classes and methods have been removed or renamed since the pre-1.0 releases.

Related Links
=============

* `Sauce Labs <https://saucelabs.com>`_
* `Sauce Labs REST API documentation <http://saucelabs.com/docs/rest>`_
* `Python bindings for Selenium WebDriver <http://pypi.python.org/pypi/selenium>`_
