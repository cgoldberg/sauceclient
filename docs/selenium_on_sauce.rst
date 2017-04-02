===============================================
Selenium WebDriver in Python (local and remote)
===============================================

Requirements
============

 * Python 2.7 or 3.x
 * Selenium 2.x bindings (``pip install selenium``)

Selenium - Local WebDriver example
==================================

Let's start with a very simple Selenium WebDriver example...

consider the following Python code::

    #!/usr/bin/env python

    from selenium import webdriver
    
    driver = webdriver.Firefox()
    driver.get('http://saucelabs.com/test/guinea-pig')
    driver.quit()

This code uses ``webdriver.Firefox()``, to invoke the local FireFox driver.

Selenium - Remote WebDriver example
===================================

Instead of running locally via ``webdriver.Firefox()``, we can use 
``webdriver.Remote()``, and have it execute *from* a remote machine 
running Selenium Server. In this case, the Sauce Labs cloud::

    #!/usr/bin/env python
    
    from selenium import webdriver

    SAUCE_USERNAME = 'your-username-string'
    SAUCE_ACCESS_KEY = 'your-access-key-string'
    
    driver = webdriver.Remote(
        desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
        command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' %
        (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
    )
    driver.get('http://saucelabs.com/test/guinea-pig')
    id = self.driver.session_id
    print 'Link to your job: https://saucelabs.com/jobs/%s' % id
    driver.quit()

Running a Test From Local WebDriver
===================================

The following Python script executes a simple test against a remote web server.
It drives the local FireFox browser::

    #!/usr/bin/env python

    import unittest
    from selenium import webdriver


    class Selenium2OnLocal(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Firefox()
            
        def test_from_local(self):
            self.driver.get('http://saucelabs.com/test/guinea-pig')
            self.assertEqual('I am a page title - Sauce Labs', self.driver.title)
            body = self.driver.find_element_by_css_selector('body')
            self.assertIn('This page is a Selenium sandbox', body.text)

        def tearDown(self):
            self.driver.quit()


    if __name__ == '__main__':
        unittest.main()

Running a Test From Sauce Labs
==============================

Similar Python script as above, but now executing from Sauce Labs cloud. Notice
the use of ``webdriver.Remote()`` as a replacement driver::

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

        def test_from_sauce(self):
            self.driver.get('http://saucelabs.com/test/guinea-pig')
            self.assertEqual('I am a page title - Sauce Labs', self.driver.title)
            body = self.driver.find_element_by_css_selector('body')
            self.assertIn('This page is a Selenium sandbox', body.text)

        def tearDown(self):
            id = self.driver.session_id
            print 'Link to your job: https://saucelabs.com/jobs/%s' % id
            self.driver.quit()


    if __name__ == '__main__':
        unittest.main()


