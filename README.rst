===========
sauceclient
===========

**Python client library for Sauce Labs API.**

.. image:: https://travis-ci.org/cgoldberg/sauceclient.svg?branch=master
    :target: https://travis-ci.org/cgoldberg/sauceclient

Info
=====

 * Author: `Corey Goldberg <https://github.com/cgoldberg>`_ (2013-2017)
 * Docs: https://readthedocs.org/projects/sauceclient
 * Releases: https://pypi.python.org/pypi/sauceclient
 * Dev: https://github.com/cgoldberg/sauceclient
 * License: Apache v2.0

About sauceclient
=================

*sauceclient* is a Python client library for Sauce Labs API.  You can manage
a Selenium test environment and retrieve test assets from Sauce.

The API gives remote access to:

 * Test Jobs & Assets (Results, Logs, Videos, Screenshots)
 * Account
 * Platform Information
 * JavaScript Unit Tests
 * Temporary Storage
 * Tunnels

Note: *sauceclient* is not used for running tests on Sauce Labs' services.
Test execution is handled by `Selenium WebDriver`_.

.. _Selenium WebDriver: selenium_on_sauce.html

About Sauce Labs
================

`Sauce Labs <https://saucelabs.com>`_ is a service for running remote Selenium
WebDriver tests. It has VM's with 800+ browser/OS combinations, allowing
comprehensive cross-browser cross-platform test coverage.

Install
=======

 * with `pip`::

      pip install sauceclient

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

Related Links
=============

 * `Sauce Labs <https://saucelabs.com>`_
 * `Sauce Labs REST API documentation <http://saucelabs.com/docs/rest>`_
 * `Python bindings for Selenium WebDriver <http://pypi.python.org/pypi/selenium>`_

Compatibility Note
==================

Due to changes in the SauceLabs REST API, some of sauceclient's
classes and methods have been changed or renamed since the pre-1.0 release.
