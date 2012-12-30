===========
sauceclient
===========

*Python client library for Sauce Labs API.*

----

Work in Progress...

 - @cgoldberg (12/30/2012)
 
----

-----------------
about sauceclient
-----------------

`sauceclient` is for interacting with Sauce Labs to retrieve and update information about resources such as:

 * Information
 * Jobs
 * Provisioning
 * Usage

`sauceclient` is *not* for running your tests on Sauce Labs service.  That is done via Selenium WebDriver.

---------------------------------
Sauce Labs REST API documentation
---------------------------------

* http://saucelabs.com/docs/rest

-------------------------
example using sauceclient
-------------------------

* accessing publicly::

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

----------------------------------
running the sauceclient unit tests
----------------------------------

* clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git
    $ cd sauceclient

* tests are located in::

    sauceclient/test_sauceclient.py
    
* edit `test_sauceclient.py`, and change the 
  test parameters to match your Sauce Labs account info::

    SAUCE_USERNAME = 'your-username-string'
    SAUCE_ACCESS_KEY = 'your-access-key-string'
    TEST_JOB_ID = 'a-valid-test-job-id'

* run tests by executing `test_sauceclient.py`, or using `unittest` discovery::

    $ python -m unittest discover
