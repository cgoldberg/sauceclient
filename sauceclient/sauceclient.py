#!/usr/bin/env python
#
#   Copyright (c) 2012 Corey Goldberg
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
import httplib
import json


__version__ = '0.1.0dev'


SAUCE_USERNAME = None
SAUCE_ACCESS_KEY = None


def set_credentials(sauce_username, sauce_access_key):
    """Set credentials for Sauce Labs authorization."""
    global SAUCE_USERNAME
    global SAUCE_ACCESS_KEY
    SAUCE_USERNAME = sauce_username
    SAUCE_ACCESS_KEY = sauce_access_key

def _make_headers(sauce_username, sauce_access_key):
    base64string = base64.encodestring(
        '%s:%s' % (sauce_username, sauce_access_key)
    )[:-1]
    headers = {
        'Authorization': 'Basic %s' % base64string,
        'Content-Type': 'application/json',
    }
    return headers
    
def _sauce_request(method, url, headers, body=None):
    connection = httplib.HTTPSConnection('saucelabs.com')
    connection.request(method, url, body, headers=headers)
    response = connection.getresponse()
    json_data = response.read()
    connection.close()
    if response.status != 200:
        raise Exception('%s: %s.\nSauce Status NOT OK' %
                        (response.status, response.reason))
    return json_data
    

class Jobs(object):

    def __init__(self):
        self.sauce_username = SAUCE_USERNAME
        self.sauce_access_key = SAUCE_ACCESS_KEY
        if not all((self.sauce_username, self.sauce_access_key)):
            raise SystemExit('Error: please set credentials')
        self.headers = _make_headers(
            self.sauce_username, self.sauce_access_key
        )
    
    def list_job_ids(self):
        """List all jobs id's belonging to the user."""
        method = 'GET'
        url = '/rest/v1/%s/jobs' % self.sauce_username
        json_data = _sauce_request(method, url, self.headers)
        jobs = json.loads(json_data)
        job_ids = [attr['id'] for attr in jobs]
        return job_ids

    def list_jobs(self):
        """List all jobs belonging to the user."""
        method = 'GET'
        url = '/rest/v1/%s/jobs' % self.sauce_username
        url += '?full=true'
        json_data = _sauce_request(method, url, self.headers)
        jobs = json.loads(json_data)
        return jobs

    def get_job_attributes(self, job_id):
        """Get information for the specified job."""
        method = 'GET'
        url = '/rest/v1/%s/jobs/%s' % (self.sauce_username, job_id)
        json_data = _sauce_request(method, url, self.headers)
        attributes = json.loads(json_data)
        return attributes

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
        url = '/rest/v1/%s/jobs/%s' % (self.sauce_username, job_id)
        json_data = _sauce_request(method, url, self.headers, body=body)
        attributes = json.loads(json_data)
        return attributes


class Provisioning(object):
    
    def __init__(self):
        self.sauce_username = SAUCE_USERNAME
        self.sauce_access_key = SAUCE_ACCESS_KEY
        if not all((self.sauce_username, self.sauce_access_key)):
            raise SystemExit('Error: please set credentials')
        self.headers = _make_headers(
            self.sauce_username, self.sauce_access_key
        )
            
    def get_account_details(self):
        """Access account details."""
        method = 'GET'
        url = '/rest/v1/users/%s' % self.sauce_username
        json_data = _sauce_request(method, url, self.headers)
        attributes = json.loads(json_data)
        return attributes

    def get_account_limits(self):
        """Access account limits."""
        method = 'GET'
        url = '/rest/v1/%s/limits' % self.sauce_username
        json_data = _sauce_request(method, url, self.headers)
        attributes = json.loads(json_data)
        return attributes
