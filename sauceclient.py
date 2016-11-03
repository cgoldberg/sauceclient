#!/usr/bin/env python
#
# Copyright (c) 2013 Corey Goldberg
#
#   This file is part of: sauceclient
#   https://github.com/cgoldberg/sauceclient
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   ----------------
#
#   Sauce Labs REST API documentation:
#     http://saucelabs.com/docs/rest


import base64
import hmac
import json
import os
import sys
import urllib
from hashlib import md5

__version__ = '0.2.1'

is_py2 = sys.version_info.major is 2

if is_py2:
    import httplib as http_client
    from urllib import urlretrieve
else:
    import http.client as http_client
    from urllib.request import urlretrieve


def json_loads(json_data):
    if not is_py2:
        json_data = json_data.decode(encoding='UTF-8')
    return json.loads(json_data)

def safe_str(value):
    if not is_py2:
        value = bytes(value, 'utf-8')
    return value

class SauceException(Exception):
    def __init__(self, *args, **kwargs):
        super(SauceException, self).__init__(*args)
        self.response = kwargs.get('response')

class SauceClient(object):
    def __init__(self, sauce_username=None, sauce_access_key=None):
        self.sauce_username = sauce_username
        self.sauce_access_key = sauce_access_key
        self.headers = self.make_headers()
        self.account = Account(self)
        self.information = Information(self)
        self.javascript = JavaScriptTests(self)
        self.jobs = Jobs(self)
        self.storage = Storage(self)
        self.tunnels = Tunnels(self)
        #self.provisioning = Accounts(self)
        #self.usage = Usage(self)

    def make_headers(self):
        base64string = self.get_encoded_auth_string()
        headers = {
            'Authorization': 'Basic %s' % base64string,
            'Content-Type': 'application/json',
        }
        return headers

    def request(self, method, url, body=None, content_type=None):
        headers = self.headers
        if content_type:
            headers['Content-Type'] = content_type
        connection = http_client.HTTPSConnection('saucelabs.com')
        connection.request(method, url, body, headers=headers)
        response = connection.getresponse()
        json_data = json_loads(response.read())
        connection.close()
        if response.status not in [200, 201]:
            raise SauceException('%s: %s.\nSauce Status NOT OK' %
                                 (response.status, response.reason), response=response)
        return json_data

    def download(self, url, filepath):
        urlretrieve(url, filepath)
        headers = self.headers
        if content_type:
            headers['Content-Type'] = content_type
        connection = http_client.HTTPSConnection('saucelabs.com')
        connection.request(method, url, headers=headers)
        response = connection.getresponse()
        json_data = json_loads(response.read())
        connection.close()
        if response.status not in [200, 201]:
            raise SauceException('%s: %s.\nSauce Status NOT OK' %
                                 (response.status, response.reason), response=response)
        return json_data

    def get_encoded_auth_string(self):
        auth_info = '%s:%s' % (self.sauce_username, self.sauce_access_key)
        if is_py2:
            base64string = base64.encodestring(auth_info)[:-1]
        else:
            base64string = base64.b64encode(auth_info.encode(encoding='UTF-8')).decode(encoding='UTF-8')
        return base64string


class Account(object):
    """Account Methods

    These methods provide user account information and management.
    - https://wiki.saucelabs.com/display/DOCS/Account+Methods
    """
    def __init__(self, client):
        self.client = client

    def get_user(self):
        """Access basic account information."""
        method = 'GET'
        url = '/rest/v1/users/{}'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def create_user(self, username, password, name, email):
        """Create a sub account."""
        method = 'POST'
        url = '/rest/v1/users/{}'.format(self.client.sauce_username)
        body = json.dumps({
            'username': username,
            'password': password,
            'name': name,
            'email': email,
        })
        return self.client.request(method, url, body)

    def get_concurrency(self):
        """Check account concurrency limits."""
        method = 'GET'
        url = '/rest/v1.1/users/{}/concurrency'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def get_subaccounts(self):
        """Get a list of sub accounts associated with a parent account."""
        method = 'GET'
        url = '/rest/v1/users/{}/list-subaccounts'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def get_siblings(self):
        """Get a list of sibling accounts associated with provided account."""
        method = 'GET'
        url = '/rest/v1.1/users/{}/siblings'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def get_subaccount_info(self):
        """Get information about a sub account."""
        method = 'GET'
        url = '/rest/v1/users/{}/subaccounts'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def change_access_key(self):
        """Change access key of your account."""
        method = 'POST'
        url = '/rest/v1/users/{}/accesskey/change'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def get_activity(self):
        """Check account concurrency limits."""
        method = 'GET'
        url = '/rest/v1/{}/activity'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def get_usage(self, start=None, end=None):
        """Access historical account usage data."""
        method = 'GET'
        url = '/rest/v1/users/{}/usage'.format(self.client.sauce_username)
        data = {}
        if start:
            data['start'] = start
        if end:
            data['end'] = end
        if data:
            url = '?'.join([url, urllib.urlencode(data)])
        return self.client.request(method, url)


class Information(object):
    """Information Methods

    Information resources are publicly available data about Sauce Lab's service.
    - https://wiki.saucelabs.com/display/DOCS/Information+Methods
    """
    def __init__(self, client):
        self.client = client

    def get_status(self):
        """Get the current status of Sauce Labs services."""
        method = 'GET'
        url = '/rest/v1/info/status'
        return self.client.request(method, url)

    def get_platforms(self, automation_api='all'):
        """Get a list of objects describing all the OS and browser platforms currently supported on Sauce Labs."""
        method = 'GET'
        url = '/rest/v1/info/platforms/{}'.format(automation_api)
        return self.client.request(method, url)

    def get_appium_eol_dates(self):
        """Get a list of Appium end-of-life dates. Dates are displayed in Unix time."""
        method = 'GET'
        url = '/rest/v1/info/platforms/appium/eol'
        return self.client.request(method, url)


class JavaScriptTests(object):
    """JavaScript Unit Testing Methods

    - https://wiki.saucelabs.com/display/DOCS/JavaScript+Unit+Testing+Methods
    """
    def __init__(self, client):
        self.client = client

    def start_js_test(self, platforms, url, framework):
        """Start your JavaScript unit tests on as many browsers as you like with a single request."""
        method = 'POST'
        url = '/rest/v1/{}/js-tests'.format(self.client.sauce_username)
        body = json.dumps({
            'platforms': platforms,
            'url': url,
            'framework': framework,
        })
        print(method)
        print(url)
        print(body)
        return self.client.request(method, url, body)

    def get_js_test_status(self, js_tests):
        """Get the status of your JS unit tests."""
        method = 'POST'
        url = '/rest/v1/{}/js-tests/status'.format(self.client.sauce_username)
        body = json.dumps({
            'js tests': js_tests,
        })
        return self.client.request(method, url, body)

class Jobs(object):
    """Job Methods

    - https://wiki.saucelabs.com/display/DOCS/Job+Methods
    """
    def __init__(self, client):
        self.client = client

    def get_jobs(self, full=None, limit=None, skip=None, start=None, end=None,
                 format=None):
        """List jobs belonging to a specific user."""
        method = 'GET'
        url = '/rest/v1/{}/jobs'.format(self.client.sauce_username)
        data = {}
        if full is not None:
            data['full'] = full
        if limit is not None:
            data['limit'] = limit
        if skip is not None:
            data['skip'] = skip
        if start is not None:
            data['from'] = start
        if end is not None:
            data['to'] = end
        if format is not None:
            data['format'] = format
        if data:
            url = '?'.join([url, urllib.urlencode(data)])
        return self.client.request(method, url)

    def update_job(self, job_id, build=None, custom_data=None,
                   name=None, passed=None, public=None, tags=None):
        """Edit an existing job."""
        method = 'PUT'
        url = '/rest/v1/{}/jobs/{}'.format(self.client.sauce_username, job_id)
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
        return self.client.request(method, url, body=body)

    def delete_job(self, job_id):
        """Removes the job from the system with all the linked assets."""
        method = 'DELETE'
        url = '/rest/v1/{}/jobs/{}'.format(self.client.sauce_username, job_id)
        return self.client.request(method, url)

    def stop_job(self, job_id):
        """Terminates a running job."""
        method = 'PUT'
        url = '/rest/v1/{}/jobs/{}/stop'.format(self.client.sauce_username, job_id)
        return self.client.request(method, url)

    def get_job_assets(self, job_id):
        """Get details about the static assets collected for a specific job."""
        method = 'GET'
        url = '/rest/v1/{}/jobs/{}/assets'.format(self.client.sauce_username, job_id)
        return self.client.request(method, url)

    def get_job_asset_url(self, job_id, filename):
        """Get details about the static assets collected for a specific job."""
        method = 'GET'
        return 'https://saucelabs.com/rest/v1/{}/jobs/{}/assets/{}'.format(self.client.sauce_username, job_id, filename)

    def download_asset_url(self, job_id, filename, download_path):
        """Get details about the static assets collected for a specific job."""
        method = 'GET'
        url = self.get_job_asset_url(job_id, filename)
        self.client.download(url, download_path)

    def delete_job_assets(self, job_id):
        """Delete all the assets captured during a test run."""
        method = 'DELETE'
        url = '/rest/v1/{}/jobs/{}/assets'.format(self.client.sauce_username, job_id)
        return self.client.request(method, url)

    def get_auth_token(self, job_id, date_range=None):
        """Get an auth token to access protected job resources.
        
        https://wiki.saucelabs.com/display/DOCS/Building+Links+to+Test+Results
        """
        key = '{}:{}'.format(self.client.sauce_username, self.client.sauce_access_key)
        if date_range:
            key = '{}:{}'.format(key, date_range)
        return {
            'token': hmac.new(safe_str(key), safe_str(job_id), md5).hexdigest()
        }

class Storage(object):
    """Temporary Storage Methods

    - https://wiki.saucelabs.com/display/DOCS/Temporary+Storage+Methods
    """
    def __init__(self, client):
        self.client = client

    def upload_file(self, filepath):
        """Uploads a file to the temporary sauce storage."""
        method = 'POST'
        filename = os.path.split(filepath)
        url = '/rest/v1/storage/{}/{}'.format(self.client.sauce_username, filename)
        body = file(filepath, "rb")
        return self.client.request(method, url, body, content_type='application/octet-stream')

    def get_stored_files(self):
        """Check which files are in your temporary storage."""
        method = 'GET'
        url = '/rest/v1/storage/{}'.format(self.client.sauce_username)
        return self.client.request(method, url)


class Tunnels(object):
    """Tunnel Methods

    - https://wiki.saucelabs.com/display/DOCS/Tunnel+Methods
    """
    def __init__(self, client):
        self.client = client

    def get_tunnels(self):
        """Retrieves all running tunnels for a specific user."""
        method = 'GET'
        url = '/rest/v1/{}/tunnels'.format(self.client.sauce_username)
        return self.client.request(method, url)

    def get_tunnel(self, tunnel_id):
        """Get information for a tunnel given its ID."""
        method = 'GET'
        url = '/rest/v1/{}/tunnels/{}'.format(self.client.sauce_username, tunnel_id)
        return self.client.request(method, url)

    def delete_tunnel(self, tunnel_id):
        """Get information for a tunnel given its ID."""
        method = 'DELETE'
        url = '/rest/v1/{}/tunnels/{}'.format(self.client.sauce_username, tunnel_id)
        return self.client.request(method, url)
