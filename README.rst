===========
sauceclient
===========

*Python client library for Sauce Labs API.*

----

Work in Progress...

 - @cgoldberg (12/29/2012)
 
----

-----------------
about sauceclient
-----------------

`sauceclient` is *not* for running your tests on Sauce Labs service.  That is done via Selenium WebDriver.

`sauceclient` is for interacting with Sauce Labs to retrieve and update information about resources such as:

 * Provisioning
 * Usage
 * Jobs
 * Information

Sauce Labs REST API documentation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://saucelabs.com/docs/rest

----------------------------------
a simple example using sauceclient
----------------------------------

::
    import sauceclient

    sc = sauceclient.SauceClient(
        'sauce-username',
        'sauce-access-key',
    )
            
    job_ids = sc.jobs.list_job_ids()
    a_job = job_ids[0]
    attributes = sc.jobs.get_job_attributes(a_job)

----------------------------------
running the sauceclient unit tests
----------------------------------

* clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git

* edit `./sauceclient/sauceclient/test_sauceclient.py`, and change the 
  test parameters to match your Sauce Labs account info::

    SAUCE_USERNAME = 'your-username-string'
    SAUCE_ACCESS_KEY = 'your-access-key-string'
    TEST_JOB_ID = 'a-valid-test-job-id'

* run tests using standard `unittest` discovery::

    $ python unittest -m discover
