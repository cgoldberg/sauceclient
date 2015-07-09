===========
sauceclient
===========

**Python client library for Sauce Labs API.**

-------------
documentation
-------------

**please see docs at: http://cgoldberg.github.io/sauceclient/**

-----------------
about sauceclient
-----------------

``sauceclient`` is a Python client library used to retrieve and update information about resources.  The Sauce Labs API provides the following resources:

* Information
* Jobs
* Provisioning
* Usage


``sauceclient`` is *not* for running your tests on Sauce Labs'
service.  (That is done via Selenium WebDriver).

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

