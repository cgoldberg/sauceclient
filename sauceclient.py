#!/usr/bin/env python
"""Sauce Labs REST API client

   Copyright (c) 2013-2017 Corey Goldberg

   This file is part of: sauceclient
   https://github.com/cgoldberg/sauceclient

   License: Apache Version 2.0
   http://www.apache.org/licenses/LICENSE-2.0

   Sauce Labs REST API documentation:
   http://saucelabs.com/docs/rest
"""

import base64
import hmac
import json
import os
from hashlib import md5

try:
    import http.client as http_client
    from urllib.parse import urlencode
except ImportError:
    import httplib as http_client
    from urllib import urlencode


__version__ = '1.0.1'


class SauceException(Exception):
    """SauceClient exception."""

    def __init__(self, *args, **kwargs):
        """Initialize class."""
        super(SauceException, self).__init__(*args)
        self.response = kwargs.get('response')


class SauceClient(object):
    """SauceClient class."""

    def __init__(self, sauce_username=None, sauce_access_key=None, apibase=None):
        """Initialize class."""
        self.sauce_username = sauce_username
        self.sauce_access_key = sauce_access_key
        self.apibase = apibase or 'saucelabs.com'
        self.headers = self.make_headers()
        self.account = Account(self)
        self.information = Information(self)
        self.javascript = JavaScriptTests(self)
        self.jobs = Jobs(self)
        self.storage = Storage(self)
        self.tunnels = Tunnels(self)
        self.analytics = Analytics(self)

    def get_auth_string(self):
        """Create auth string from credentials."""
        auth_info = '{}:{}'.format(self.sauce_username, self.sauce_access_key)
        return base64.b64encode(auth_info.encode('utf-8')).decode('utf-8')

    def make_headers(self, content_type='application/json'):
        """Create content-type header."""
        return {
            'Content-Type': content_type,
        }

    def make_auth_headers(self, content_type):
        """Add authorization header."""
        headers = self.make_headers(content_type)
        headers['Authorization'] = 'Basic {}'.format(self.get_auth_string())
        return headers

    def request(self, method, url, body=None, content_type='application/json'):
        """Send http request."""
        headers = self.make_auth_headers(content_type)
        connection = http_client.HTTPSConnection(self.apibase)
        connection.request(method, url, body, headers=headers)
        response = connection.getresponse()
        data = response.read()
        connection.close()
        if response.status not in [200, 201]:
            raise SauceException('{}: {}.\nSauce Status NOT OK'.format(
                response.status, response.reason), response=response)
        return json.loads(data.decode('utf-8'))


class Account(object):
    """Account Methods

    These methods provide user account information and management.
    - https://wiki.saucelabs.com/display/DOCS/Account+Methods
    """
    def __init__(self, client):
        """Initialize class."""
        self.client = client

    def get_user(self):
        """Access basic account information."""
        method = 'GET'
        endpoint = '/rest/v1/users/{}'.format(self.client.sauce_username)
        return self.client.request(method, endpoint)

    def create_user(self, username, password, name, email):
        """Create a sub account."""
        method = 'POST'
        endpoint = '/rest/v1/users/{}'.format(self.client.sauce_username)
        body = json.dumps({'username': username, 'password': password,
                           'name': name, 'email': email, })
        return self.client.request(method, endpoint, body)

    def get_concurrency(self):
        """Check account concurrency limits."""
        method = 'GET'
        endpoint = '/rest/v1.1/users/{}/concurrency'.format(
            self.client.sauce_username)
        return self.client.request(method, endpoint)

    def get_subaccounts(self):
        """Get a list of sub accounts associated with a parent account."""
        method = 'GET'
        endpoint = '/rest/v1/users/{}/list-subaccounts'.format(
            self.client.sauce_username)
        return self.client.request(method, endpoint)

    def get_siblings(self):
        """Get a list of sibling accounts associated with provided account."""
        method = 'GET'
        endpoint = '/rest/v1.1/users/{}/siblings'.format(
            self.client.sauce_username)
        return self.client.request(method, endpoint)

    def get_subaccount_info(self):
        """Get information about a sub account."""
        method = 'GET'
        endpoint = '/rest/v1/users/{}/subaccounts'.format(
            self.client.sauce_username)
        return self.client.request(method, endpoint)

    def change_access_key(self):
        """Change access key of your account."""
        method = 'POST'
        endpoint = '/rest/v1/users/{}/accesskey/change'.format(
            self.client.sauce_username)
        return self.client.request(method, endpoint)

    def get_activity(self):
        """Check account concurrency limits."""
        method = 'GET'
        endpoint = '/rest/v1/{}/activity'.format(self.client.sauce_username)
        return self.client.request(method, endpoint)

    def get_usage(self, start=None, end=None):
        """Access historical account usage data."""
        method = 'GET'
        endpoint = '/rest/v1/users/{}/usage'.format(self.client.sauce_username)
        data = {}
        if start:
            data['start'] = start
        if end:
            data['end'] = end
        if data:
            endpoint = '?'.join([endpoint, urlencode(data)])
        return self.client.request(method, endpoint)

class Analytics(object):
    """Analytics Methods

    These methods provide user account information and management.
    - https://wiki.saucelabs.com/display/DOCS/Analytics+Methods
    """
    def __init__(self, client):
        self.client = client

    def get_test_trends(self, start=None, end=None, interval=None, time_range=None, scope=None,
                        owner=None, status=None, pretty=False, os=None,
                        browser=None):
        method = 'GET'
        endpoint = '/rest/v1/analytics/trends/tests'
        data = {}

        if time_range:
            data['time_range'] = time_range
        if start:
            data['start'] = start
        if end:
            data['end'] = end
        if interval:
            data['interval'] = interval
        if scope:
            data['scope'] = scope
        if owner:
            data['owner'] = owner
        if status:
            data['status'] = status
        if pretty:
            data['pretty'] = ''
        if os:
            data['os'] = os
        if browser:
            data['browser'] = browser

        endpoint = '?'.join([endpoint, urlencode(data)])
        return self.client.request(method, endpoint)
    def get_error_trends(self, start=None, end=None, time_range=None, scope=None,
                        owner=None, status=None, pretty=False, os=None,
                        browser=None):
        method = 'GET'
        endpoint = '/rest/v1/analytics/trends/errors'
        data = {}

        if time_range:
            data['time_range'] = time_range
        if start:
            data['start'] = start
        if end:
            data['end'] = end
        if scope:
            data['scope'] = scope
        if owner:
            data['owner'] = owner
        if status:
            data['status'] = status
        if pretty:
            data['pretty'] = ''
        if os:
            data['os'] = os
        if browser:
            data['browser'] = browser

        endpoint = '?'.join([endpoint, urlencode(data)])
        return self.client.request(method, endpoint)

    def get_build_trends(self, start=None, end=None, time_range=None, scope=None,
                        owner=None, status=None, pretty=False, os=None,
                        browser=None):
        method = 'GET'
        endpoint = '/rest/v1/analytics/trends/builds_tests'
        data = {}

        if time_range:
            data['time_range'] = time_range
        if start:
            data['start'] = start
        if end:
            data['end'] = end
        if scope:
            data['scope'] = scope
        if owner:
            data['owner'] = owner
        if status:
            data['status'] = status
        if pretty:
            data['pretty'] = ''
        if os:
            data['os'] = os
        if browser:
            data['browser'] = browser

        endpoint = '?'.join([endpoint, urlencode(data)])
        return self.client.request(method, endpoint)

    def get_tests(self, start=None, end=None, size=None, time_range=None, scope=None,
                  owner=None, status=None, pretty=False, error=None, build=None,
                  skip=None,missing_build=False):

        method = 'GET'
        endpoint = '/rest/v1/analytics/tests'
        data = {}

        if time_range:
            data['time_range'] = time_range
        if start:
            data['start'] = start
        if end:
            data['end'] = end
        if size:
            data['size'] = size
        if scope:
            data['scope'] = scope
        if owner:
            data['owner'] = owner
        if status:
            data['status'] = status
        if pretty:
            data['pretty'] = ''
        if error:
            data['error'] = error
        if build:
            data['build'] = build
        #from is a reserved keyword, using skip instead
        if skip:
            data['from'] = skip
        if missing_build:
            data['missing_build'] = ''


        endpoint = '?'.join([endpoint, urlencode(data)])
        return self.client.request(method, endpoint)

    def get_concurrency(self, start=None, end=None, interval=None, time_range=None, scope=None,
                        owner=None, status=None, pretty=False):

        method = 'GET'
        endpoint = '/rest/v1/analytics/insights/concurrency'
        data={}


        if time_range:
            data['time_range'] = time_range
        if start:
            data['start'] = start
        if end:
            data['end'] = end
        if interval:
            data['interval'] = interval
        if scope:
            data['scope'] = scope
        if owner:
            data['owner'] = owner
        if status:
            data['status'] = status
        if pretty:
            data['pretty'] = ''


        endpoint = '?'.join([endpoint, urlencode(data)])
        return self.client.request(method, endpoint)



class Information(object):
    """Information Methods

    Information resources are publicly available data about
    Sauce Lab's service.
    - https://wiki.saucelabs.com/display/DOCS/Information+Methods
    """
    def __init__(self, client):
        """Initialize class."""
        self.client = client

    def get_status(self):
        """Get the current status of Sauce Labs services."""
        method = 'GET'
        endpoint = '/rest/v1/info/status'
        return self.client.request(method, endpoint)

    def get_platforms(self, automation_api='all'):
        """Get a list of objects describing all the OS and browser platforms
        currently supported on Sauce Labs."""
        method = 'GET'
        endpoint = '/rest/v1/info/platforms/{}'.format(automation_api)
        return self.client.request(method, endpoint)

    def get_appium_eol_dates(self):
        """Get a list of Appium end-of-life dates. Dates are displayed in Unix
        time."""
        method = 'GET'
        endpoint = '/rest/v1/info/platforms/appium/eol'
        return self.client.request(method, endpoint)


class JavaScriptTests(object):
    """JavaScript Unit Testing Methods

    - https://wiki.saucelabs.com/display/DOCS/JavaScript+Unit+Testing+Methods
    """
    def __init__(self, client):
        self.client = client

    def js_tests(self, platforms, url, framework):
        """Start your JavaScript unit tests on as many browsers as you like
        with a single request."""
        method = 'POST'
        endpoint = '/rest/v1/{}/js-tests'.format(self.client.sauce_username)
        body = json.dumps({'platforms': platforms, 'url': url,
                           'framework': framework, })
        return self.client.request(method, endpoint, body)

    def js_tests_status(self, js_tests):
        """Get the status of your JS unit tests."""
        method = 'POST'
        endpoint = '/rest/v1/{}/js-tests/status'.format(
            self.client.sauce_username)
        body = json.dumps({
            'js tests': js_tests,
        })
        return self.client.request(method, endpoint, body)


class Jobs(object):
    """Job Methods

    - https://wiki.saucelabs.com/display/DOCS/Job+Methods
    """
    def __init__(self, client):
        """Initialize class."""
        self.client = client

    def get_jobs(self, full=None, limit=None, skip=None, start=None, end=None,
                 job_name=None, output_format=None):
        """List jobs belonging to a specific user."""
        method = 'GET'
        endpoint = '/rest/v1/{}/jobs'.format(self.client.sauce_username)
        data = {}
        if full is not None:
            data['full'] = full
        if limit is not None:
            data['limit'] = limit
        if skip is not None:
            data['skip'] = skip
        if job_name is not None:
            data['name'] = job_name
        if start is not None:
            data['from'] = start
        if end is not None:
            data['to'] = end
        if output_format is not None:
            data['format'] = output_format
        if data:
            endpoint = '?'.join([endpoint, urlencode(data)])
        return self.client.request(method, endpoint)

    def get_job(self, job_id):
        """Retreive a single job."""
        method = 'GET'
        endpoint = '/rest/v1/{}/jobs/{}'.format(self.client.sauce_username,
                                                job_id)
        return self.client.request(method, endpoint)

    def update_job(self, job_id, build=None, custom_data=None,
                   name=None, passed=None, public=None, tags=None):
        """Edit an existing job."""
        method = 'PUT'
        endpoint = '/rest/v1/{}/jobs/{}'.format(self.client.sauce_username,
                                                job_id)
        data = {}
        if build is not None:
            data['build'] = build
        if custom_data is not None:
            data['custom-data'] = custom_data
        if name is not None:
            data['name'] = name
        if passed is not None:
            data['passed'] = passed
        if public is not None:
            data['public'] = public
        if tags is not None:
            data['tags'] = tags
        body = json.dumps(data)
        return self.client.request(method, endpoint, body=body)

    def delete_job(self, job_id):
        """Removes the job from the system with all the linked assets."""
        method = 'DELETE'
        endpoint = '/rest/v1/{}/jobs/{}'.format(self.client.sauce_username,
                                                job_id)
        return self.client.request(method, endpoint)

    def stop_job(self, job_id):
        """Terminates a running job."""
        method = 'PUT'
        endpoint = '/rest/v1/{}/jobs/{}/stop'.format(
            self.client.sauce_username, job_id)
        return self.client.request(method, endpoint)

    def get_job_assets(self, job_id):
        """Get details about the static assets collected for a specific job."""
        method = 'GET'
        endpoint = '/rest/v1/{}/jobs/{}/assets'.format(
            self.client.sauce_username, job_id)
        return self.client.request(method, endpoint)

    def get_job_asset_url(self, job_id, filename):
        """Get details about the static assets collected for a specific job."""
        return 'https://saucelabs.com/rest/v1/{}/jobs/{}/assets/{}'.format(
            self.client.sauce_username, job_id, filename)

    def delete_job_assets(self, job_id):
        """Delete all the assets captured during a test run."""
        method = 'DELETE'
        endpoint = '/rest/v1/{}/jobs/{}/assets'.format(
            self.client.sauce_username, job_id)
        return self.client.request(method, endpoint)

    def get_auth_token(self, job_id, date_range=None):
        """Get an auth token to access protected job resources.

        https://wiki.saucelabs.com/display/DOCS/Building+Links+to+Test+Results
        """
        key = '{}:{}'.format(self.client.sauce_username,
                             self.client.sauce_access_key)
        if date_range:
            key = '{}:{}'.format(key, date_range)
        return hmac.new(key.encode('utf-8'), job_id.encode('utf-8'),
                        md5).hexdigest()


class Storage(object):
    """Temporary Storage Methods

    - https://wiki.saucelabs.com/display/DOCS/Temporary+Storage+Methods
    """
    def __init__(self, client):
        """Initialize class."""
        self.client = client

    def upload_file(self, filepath, overwrite=True):
        """Uploads a file to the temporary sauce storage."""
        method = 'POST'
        filename = os.path.split(filepath)[1]
        endpoint = '/rest/v1/storage/{}/{}?overwrite={}'.format(
            self.client.sauce_username, filename, "true" if overwrite else "false")
        with open(filepath, 'rb') as filehandle:
            body = filehandle.read()
        return self.client.request(method, endpoint, body,
                                   content_type='application/octet-stream')

    def get_stored_files(self):
        """Check which files are in your temporary storage."""
        method = 'GET'
        endpoint = '/rest/v1/storage/{}'.format(self.client.sauce_username)
        return self.client.request(method, endpoint)


class Tunnels(object):
    """Tunnel Methods

    - https://wiki.saucelabs.com/display/DOCS/Tunnel+Methods
    """
    def __init__(self, client):
        """Initialize class."""
        self.client = client

    def get_tunnels(self):
        """Retrieves all running tunnels for a specific user."""
        method = 'GET'
        endpoint = '/rest/v1/{}/tunnels'.format(self.client.sauce_username)
        return self.client.request(method, endpoint)

    def get_tunnel(self, tunnel_id):
        """Get information for a tunnel given its ID."""
        method = 'GET'
        endpoint = '/rest/v1/{}/tunnels/{}'.format(
            self.client.sauce_username, tunnel_id)
        return self.client.request(method, endpoint)

    def delete_tunnel(self, tunnel_id):
        """Get information for a tunnel given its ID."""
        method = 'DELETE'
        endpoint = '/rest/v1/{}/tunnels/{}'.format(
            self.client.sauce_username, tunnel_id)
        return self.client.request(method, endpoint)
