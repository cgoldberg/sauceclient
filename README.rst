===========
sauceclient
===========

*Python client library for Sauce Labs API.*

----

Work in Progress...

 - @cgoldberg (12/25/2012)
 
----

-----------------
About sauceclient
-----------------

sauceclient is *not* for running your tests on Sauce Labs service.  That is done via Selenium WebDriver.

sauceclient is for interacting with Sauce Labs to retrieve and update information about resources such as:

 * Provisioning
 * Usage
 * Jobs
 * Tunnels
 * Information
 
------------------------
About Selenium WebDriver
------------------------


------------------------------------
Running a Test Using Local WebDriver
------------------------------------

The following Python script executes a simple test against the Sauce Labs sandbox server.  It drives your local FireFox browser.

.. code:: Python

    #!/usr/bin/env python

    import unittest
    from selenium import webdriver


    class Selenium2OnLocal(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)

        def test_from_local(self):
            self.driver.get('http://saucelabs.com/test/guinea-pig')
            self.assertEqual('I am a page title - Sauce Labs', self.driver.title)
            body = self.driver.find_element_by_xpath('//body')
            self.assertIn('I am some page content', body.text)

        def tearDown(self):
            self.driver.quit()


    if __name__ == '__main__':
        unittest.main()

------------------------------
Running a Test From Sauce Labs
------------------------------

Similar Python script as above, but now executing from Sauce Labs cloud.  Notice the use of `webdriver.Remote()` as a replacement driver.

.. code:: Python

    #!/usr/bin/env python

    import unittest
    from selenium import webdriver


    SAUCE_USERNAME = 'your-username-string'
    SAUCE_ACCESS_KEY = 'your-access-key-string'


    class Selenium2OnSauce(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Remote(
                desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
                command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' %
                (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
            )
            self.driver.implicitly_wait(30)

        def test_from_sauce(self):
            self.driver.get('http://saucelabs.com/test/guinea-pig')
            self.assertEqual('I am a page title - Sauce Labs', self.driver.title)
            body = self.driver.find_element_by_xpath('//body')
            self.assertIn('I am some page content', body.text)

        def tearDown(self):
            print 'Link to your job: https://saucelabs.com/jobs/%s' % \
                self.driver.session_id
            self.driver.quit()


    if __name__ == '__main__':
        unittest.main()

----

------------------------------
Running sauceclient Unit Tests
------------------------------

* clone the repo::

    $ git clone git@github.com:cgoldberg/sauceclient.git

* edit `sauceclient/sauceclient/test_sauceclient.py`, and change the 
  test account parameters to match your Sauce Labs account info::

    SAUCE_USERNAME = 'your-sauce-username'
    SAUCE_ACCESS_KEY = 'your-sauce-access-key'
    TEST_JOB_ID = 'a-valid-test-job-id'

* run tests using standard unittest discovery::

    $ python unittest -m discover
