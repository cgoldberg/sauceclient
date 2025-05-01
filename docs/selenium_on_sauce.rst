===============================================
Selenium WebDriver in Python (local and remote)
===============================================

Requirements
============

 * Python 3.9+
 * Selenium Python bindings (``pip install selenium``)

Selenium - Local WebDriver example
==================================

Let's start with a very simple Selenium WebDriver example...

Consider the following Python code::

    #!/usr/bin/env python3

    from selenium import webdriver


    driver = webdriver.Chrome()
    driver.get("https://saucelabs.com/test/guinea-pig")
    driver.quit()

This code uses ``webdriver.Chrome()``, to invoke the local Chrome driver.

Selenium - Remote WebDriver example
===================================

Instead of running locally via ``webdriver.Chrome()``, we can use
``webdriver.Remote()``, and have it execute *from* a remote machine 
running Selenium Server. In this case, the Sauce Labs cloud::

    #!/usr/bin/env python3

    import os

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options


    options = Options()
    options.browser_version = "latest"
    options.platform_name = "Windows 11"
    options.add_argument("--headless=new")

    sauce_options = {"username": os.environ["SAUCE_USERNAME"],
                     "accessKey": os.environ["SAUCE_ACCESS_KEY"],
                     "name": "my_first_test"}

    options.set_capability("sauce:options", sauce_options)
    sauce_url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"

    driver = webdriver.Remote(command_executor=sauce_url, options=options)
    driver.get("https://saucelabs.com/test/guinea-pig")
    driver.quit()

Running a Test From Local WebDriver
===================================

The following Python script executes a simple test against a remote web server.
It drives the local Chrome browser::

    #!/usr/bin/env python3

    import unittest

    from selenium import webdriver
    from selenium.webdriver.common.by import By


    class SeleniumLocalTest(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Chrome()
            
        def test_from_local(self):
            self.driver.get("https://saucelabs.com/test/guinea-pig")
            self.assertEqual("I am a page title - Sauce Labs", self.driver.title)
            body = self.driver.find_element(By.CSS_SELECTOR("body")
            self.assertIn("This page is a Selenium sandbox", body.text)

        def tearDown(self):
            self.driver.quit()


    if __name__ == "__main__":
        unittest.main()

Running a Test From Sauce Labs
==============================

Similar Python script as above, but now executing from Sauce Labs cloud. Notice
the use of ``webdriver.Remote()`` as a replacement driver::

    #!/usr/bin/env python3

    import os
    import unittest

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options


    class SeleniumSauceTest(unittest.TestCase):

        def setUp(self):
            options = Options()
            options.browser_version = "latest"
            options.platform_name = "Windows 11"
            options.add_argument("--headless=new")
            sauce_options = {"username": os.environ["SAUCE_USERNAME"],
                             "accessKey": os.environ["SAUCE_ACCESS_KEY"],
                             "name": "my_first_test"}
            options.set_capability("sauce:options", sauce_options)
            sauce_url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"
            self.driver = webdriver.Remote(command_executor=sauce_url, options=options)

        def test_from_sauce(self):
            self.driver.get("https://saucelabs.com/test/guinea-pig")
            self.assertEqual("I am a page title - Sauce Labs", self.driver.title)
            body = self.driver.find_element(By.CSS_SELECTOR("body")
            self.assertIn("This page is a Selenium sandbox", body.text)

        def tearDown(self):
            self.driver.quit()


    if __name__ == "__main__":
        unittest.main()
