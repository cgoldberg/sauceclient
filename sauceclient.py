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
import sys
import json

__version__ = '0.2.1'

is_py2 = sys.version_info.major is 2

if is_py2:
    import httplib as http_client
else:
    import http.client as http_client


def json_loads(json_data):
    if not is_py2:
        json_data = json_data.decode(encoding='UTF-8')
    return json.loads(json_data)

class SauceException(Exception):
    def __init__(self, *args, **kwargs):
        super(SauceException, self).__init__(*args)
        self.response = kwargs.get('response')

class SauceClient(object):
    def __init__(self, sauce_username=None, sauce_access_key=None):
        self.sauce_username = sauce_username
        self.sauce_access_key = sauce_access_key
        self.headers = self.make_headers()
        self.information = Information(self)
        self.jobs = Jobs(self)
        self.provisioning = Provisioning(self)
        self.usage = Usage(self)

    def make_headers(self):
        base64string = self.get_encoded_auth_string()
        headers = {
            'Authorization': 'Basic %s' % base64string,
            'Content-Type': 'application/json',
        }
        return headers

    def request(self, method, url, body=None):
        connection = http_client.HTTPSConnection('saucelabs.com')
        connection.request(method, url, body, headers=self.headers)
        response = connection.getresponse()
        json_data = json_loads(response.read())
        connection.close()
        if response.status != 200:
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


class Jobs(object):
    def __init__(self, client):
        self.client = client

    def get_job_ids(self):
        """List all jobs id's belonging to the user."""
        method = 'GET'
        url = '/rest/v1/%s/jobs' % self.client.sauce_username
        jobs = self.client.request(method, url)
        return [attr['id'] for attr in jobs]

    def get_jobs(self):
        """List all jobs belonging to the user."""
        method = 'GET'
        url = '/rest/v1/%s/jobs?full=true' % self.client.sauce_username
        return self.client.request(method, url)

    def get_job_attributes(self, job_id):
        """Get information for the specified job."""
        method = 'GET'
        url = '/rest/v1/%s/jobs/%s' % (self.client.sauce_username, job_id)
        return self.client.request(method, url)

    def update_job(self, job_id, build_num=None, custom_data=None,
                   name=None, passed=None, public=None, tags=None):
        """Update attributes for the specified job."""
        content = {}
        if build_num is not None:
            content['build'] = build_num
        if custom_data is not None:
            content['custom-data'] = custom_data
        if name is not None:
            content['name'] = name
        if passed is not None:
            content['passed'] = passed
        if public is not None:
            content['public'] = public
        if tags is not None:
            content['tags'] = tags
        body = json.dumps(content)
        method = 'PUT'
        url = '/rest/v1/%s/jobs/%s' % (self.client.sauce_username, job_id)
        return self.client.request(method, url, body=body)

    def get_job_assets(self, job_id):
        """Get the list of assets for the specified job."""
        method = 'GET'
        url = '/rest/v1/%s/jobs/%s/assets' % (self.client.sauce_username,
                                              job_id)
        return self.client.request(method, url)


class Provisioning(object):
    def __init__(self, client):
        self.client = client

    def get_account_details(self):
        """Access account details."""
        method = 'GET'
        url = '/rest/v1/users/%s' % self.client.sauce_username
        return self.client.request(method, url)

    def get_account_limits(self):
        """Access account limits."""
        method = 'GET'
        url = '/rest/v1/%s/limits' % self.client.sauce_username
        return self.client.request(method, url)


class Information(object):
    def __init__(self, client):
        self.client = client

    def get_status(self):
        """Access the current status of Sauce Labs' services."""
        method = 'GET'
        url = '/rest/v1/info/status'
        return self.client.request(method, url)

    def get_platforms(self, automation_api='all'):
        """Get details of OS and browser platforms currently supported on Sauce Labs."""
        method = 'GET'
        url = '/rest/v1/info/platforms/%s' % automation_api
        return self.client.request(method, url)

    def get_appium_eol_dates(self):
        """Get details of platforms currently supported on Sauce Labs."""
        method = 'GET'
        url = '/rest/v1/info/platforms/appium/eol'
        return self.client.request(method, url)


class Usage(object):
    def __init__(self, client):
        self.client = client

    def get_current_activity(self):
        """Access current account activity.

        Returns active job counts broken down by job status and subaccount.
        """
        method = 'GET'
        url = '/rest/v1/%s/activity' % self.client.sauce_username
        return self.client.request(method, url)

    def get_historical_usage(self):
        """Access historical account usage."""
        method = 'GET'
        url = '/rest/v1/users/%s/usage' % self.client.sauce_username
        return self.client.request(method, url)
