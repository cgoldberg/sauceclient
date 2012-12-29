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


import base64
import httplib
import json


__version__ = '0.1.0dev'


def _encode_credentials(sauce_username, sauce_access_key):
    return base64.encodestring(
        '%s:%s' % (sauce_username, sauce_access_key)
    )[:-1]
        
def _sauce_request(method, url, base64string, body=None):
    headers = {'Authorization': 'Basic %s' % base64string}
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

    def __init__(self, sauce_username, sauce_access_key):
        self.sauce_username = sauce_username
        self.sauce_access_key = sauce_access_key
        self.base64string = _encode_credentials(
            sauce_username, sauce_access_key
        )
    
    def list_job_ids(self):
        """list all jobs id's belonging to the user."""
        method = 'GET'
        url = '/rest/v1/%s/jobs' % self.sauce_username
        json_data = _sauce_request(method, url, self.base64string)
        jobs = json.loads(json_data)
        job_ids = [attr['id'] for attr in jobs]
        return job_ids

    def list_jobs(self):
        """list all jobs belonging to the user."""
        method = 'GET'
        url = '/rest/v1/%s/jobs' % self.sauce_username
        url += '?full=true'
        json_data = _sauce_request(method, url, self.base64string)
        jobs = json.loads(json_data)
        return jobs

    def get_job_attributes(self, job_id):
        """get information for the specified job."""
        method = 'GET'
        url = '/rest/v1/%s/jobs/%s' % (self.sauce_username, job_id)
        json_data = _sauce_request(method, url, self.base64string)
        attributes = json.loads(json_data)
        return attributes

    def update_job(self, job_id, build_num=None, custom_data=None,
                   name=None, passed=None, public=None, tags=None):
        """update attributes for the specified job."""
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
        json_data = _sauce_request(method, url, self.base64string, body=body)
        attributes = json.loads(json_data)
        return attributes


class Provisioning(object):
    
    def __init__(self, sauce_username, sauce_access_key):
        self.sauce_username = sauce_username
        self.sauce_access_key = sauce_access_key
        self.base64string = _encode_credentials(
            sauce_username, sauce_access_key
        )

    def get_account_details(self):
        """access account details."""
        method = 'GET'
        url = '/rest/v1/users/%s' % self.sauce_username
        json_data = _sauce_request(method, url, self.base64string)
        attributes = json.loads(json_data)
        return attributes
        