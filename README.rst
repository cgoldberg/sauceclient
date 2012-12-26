===========
sauceclient
===========

-----------------------------------------
Python client library for Sauce Labs API.
-----------------------------------------

Work in Progress...

 - @cgoldberg (12/25/2012)
 
----

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running sauceclient Unit Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git

* edit `sauceclient/sauceclient/test_sauceclient.py`, and change the 
  test account parameters to match your Sauce Labs account info::

    SAUCE_USERNAME = 'your-sauce-username'
    SAUCE_ACCESS_KEY = 'your-sauce-access-key'
    TEST_JOB_ID = 'a-valid-test-job-id'

* run tests using standard unittest discovery::

    $ python unittest -m discover
