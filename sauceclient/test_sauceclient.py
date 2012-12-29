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


import sauceclient

import json
import unittest


# set these to run tests
SAUCE_USERNAME = ''
SAUCE_ACCESS_KEY = ''
TEST_JOB_ID = ''  # any valid job


class TestAPIRequest(unittest.TestCase):
    
    def setUp(self):
        self.headers = sauceclient._make_headers(
            SAUCE_USERNAME,
            SAUCE_ACCESS_KEY,
        )

    def test_headers(self):
        self.assertIsInstance(self.headers, dict)
        self.assertIn('Authorization', self.headers)
        self.assertIn('Content-Type', self.headers)
        self.assertIn('Basic', self.headers['Authorization'])
        self.assertEqual('application/json', self.headers['Content-Type'])
        
    def test_request(self):
        url = '/rest/v1/users/%s' % SAUCE_USERNAME
        json_data = sauceclient._sauce_request('GET', url, self.headers)
        self.assertIsInstance(json_data, str)
        attributes = json.loads(json_data)
        self.assertIsInstance(attributes, dict)


class TestJobs(unittest.TestCase):

    def setUp(self):
        sauceclient.set_credentials(SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        self.jobs = sauceclient.Jobs()

    def test_list_job_ids(self):
        job_ids = self.jobs.list_job_ids()
        self.assertIsInstance(job_ids, list)
        job_id = job_ids[0]
        self.assertIsInstance(job_id, unicode)
        self.assertTrue(job_id.isalnum())

    def test_list_jobs(self):
        jobs = self.jobs.list_jobs()
        self.assertIsInstance(jobs, list)
        job = jobs[0]
        self.assertIn('id', job)
        self.assertIsInstance(job['id'], unicode)
        self.assertEqual(job['owner'], SAUCE_USERNAME)

    def test_get_job_attributes(self):
        job_attributes = self.jobs.get_job_attributes(TEST_JOB_ID)
        self.assertIsInstance(job_attributes, dict)
        self.assertIn('id', job_attributes)
        self.assertEqual(job_attributes['id'], TEST_JOB_ID)

    def test_update_job(self):
        job_attributes = self.jobs.update_job(TEST_JOB_ID)
        self.assertIsInstance(job_attributes, dict)
        self.assertIn('id', job_attributes)
        self.assertEqual(job_attributes['id'], TEST_JOB_ID)

    def tearDown(self):
        SAUCE_USERNAME = None
        SAUCE_ACCESS_KEY = None


class TestProvisioning(unittest.TestCase):

    def setUp(self):
        sauceclient.set_credentials(SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        self.p = sauceclient.Provisioning()

    def test_get_account_details(self):
        account_details = self.p.get_account_details()
        self.assertIsInstance(account_details, dict)
        self.assertIn('id', account_details)
        self.assertIn('minutes', account_details)
        self.assertIn('access_key', account_details)
        self.assertIn('subscribed', account_details)
        self.assertEqual(account_details['id'], SAUCE_USERNAME)

    def test_get_account_limits(self):
        account_limits = self.p.get_account_limits()
        self.assertIsInstance(account_limits, dict)
        self.assertIn('concurrency', account_limits)
        #self.assertEqual(account_details['id'], SAUCE_USERNAME)


if __name__ == '__main__':
    if not all((SAUCE_USERNAME, SAUCE_ACCESS_KEY, TEST_JOB_ID)):
        raise SystemExit('Change your credentials (username/access-key)')
    unittest.main(verbosity=2)
