===========
sauceclient
===========

**Python client library for Sauce Labs API.**

Info
=====

 * Author: `Corey Goldberg <https://github.com/cgoldberg>`_ (2013-2025)
 * Docs: https://sauceclient.readthedocs.io
 * Releases: https://pypi.python.org/pypi/sauceclient
 * Dev: https://github.com/cgoldberg/sauceclient
 * License: Apache v2.0


About sauceclient
=================

*sauceclient* is a Python client library for Sauce Labs API. You can manage
a Selenium test environment and retrieve test assets from Sauce.

The API gives remote access to:

 * Test Jobs & Assets (Results, Logs, Videos, Screenshots)
 * Account
 * Platform Information
 * JavaScript Unit Tests
 * Temporary Storage
 * Tunnels

Note: *sauceclient* is not used for running tests on Sauce Labs' services.
Test execution is handled by your testing tool or library (Selenium,
Playwright, Cypress, Appium, etc).

About Sauce Labs
================

`Sauce Labs <https://saucelabs.com>`_ is a cloud-based service for running
remote browser-based tests. It has VM's with 800+ browser/OS combinations,
allowing comprehensive cross-browser cross-platform test coverage.

Installation
============

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
 * `Sauce Labs REST API documentation <https://docs.saucelabs.com/dev/api>`_
 * `Python bindings for Selenium WebDriver <https://pypi.org/project/selenium>`_

----

Python Module Reference
=======================

.. toctree::
    :maxdepth: 4

    sauceclient
    tests

Running Selenium WebDriver
==========================

.. toctree::
    :maxdepth: 4

    selenium_on_sauce
