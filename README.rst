===========
sauceclient
===========

**Python client library for Sauce Labs API.**

-------------
documentation
-------------

**please see docs at: http://cgoldberg.github.com/sauceclient/** 

... or generate the html documentation yourself:

 * requires: `python-sphinx <http://sphinx-doc.org>`_
 * build the docs locally::

     $ git clone git@github.com:cgoldberg/sauceclient.git
     $ cd sauceclient
     $ sphinx-build -b html doc html_docs

 * generated results end up in ``./html_docs/``

-----------------
about sauceclient
-----------------

``sauceclient`` is a Python client library, used for accessing the Sauce Labs
API to retrieve and update information about resources such as:

* Information
* Jobs
* Provisioning
* Usage

``sauceclient`` is *not* for running your tests on Sauce Labs'
service.  (That is done via Selenium WebDriver).

----------------------------------
running the sauceclient unit tests
----------------------------------

* clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git
    $ cd sauceclient

* tests are located in::

    sauceclient/test_sauceclient.py
    
* edit ``test_sauceclient.py``, and change the 
  test parameters to match your Sauce Labs account info::

    SAUCE_USERNAME = 'your-username-string'
    SAUCE_ACCESS_KEY = 'your-access-key-string'
    TEST_JOB_ID = 'a-valid-test-job-id'

* run tests by executing ``test_sauceclient.py``, or using ``unittest`` discovery::

    $ python -m unittest discover
