# sauceclient

## Python client library for Sauce Labs API

- Copyright (c) 2013-2026 [Corey Goldberg][github-home]
- Development: [GitHub][github-repo]
- Releases: [PyPI][pypi]
- Docs: [Read the Docs][readthedocs]
- License: [Apache 2.0][license]

[github-home]: https://github.com/cgoldberg
[github-repo]: https://github.com/cgoldberg/sauceclient
[pypi]: https://pypi.org/project/sauceclient
[readthedocs]: https://sauceclient.readthedocs.io/
[license]: https://raw.githubusercontent.com/cgoldberg/sauceclient/refs/heads/master/LICENSE

----

## About sauceclient

**sauceclient** is a Python client library for the Sauce Labs API. You can
manage a test environment and retrieve test assets from Sauce Labs.

The API gives remote access to:

 * Test Jobs & Assets (Results, Logs, Videos, Screenshots)
 * Account
 * Platform Information
 * JavaScript Unit Tests
 * Temporary Storage
 * Tunnels

Note: **sauceclient** is not used for running tests on Sauce Labs' services.
Test execution is handled by your testing tool or library (Selenium,
Playwright, Cypress, Appium, etc).

----

## About Sauce Labs

Sauce Labs is a cloud-based service for running remote
browser-based tests. It has VM's with 800+ browser/OS combinations, allowing
comprehensive cross-browser cross-platform test coverage.

 - [Sauce Labs][sauce-labs]
 - [Sauce Labs REST API documentation][sauce-rest-api]

[sauce-labs]: https://saucelabs.com
[sauce-rest-api]: https://docs.saucelabs.com/dev/api

----

## Installation

```
pip install sauceclient
```

----

## Example Usage

- public access:

```python
import sauceclient

sc = sauceclient.SauceClient()
status = sc.information.get_status()
```

- with authorization:

```python
import sauceclient

sc = sauceclient.SauceClient(
    "sauce-username",
    "sauce-access-key",
)
jobs = sc.jobs.get_jobs(full=True, limit=5)
```
