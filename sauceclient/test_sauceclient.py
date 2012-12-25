#!/usr/bin/env python

#  Corey Goldberg 2012


from sauceclient import SauceJobs

import json
import unittest


# set these to run tests
SAUCE_USERNAME = ''
SAUCE_ACCESS_KEY = ''
TEST_JOB_ID = ''  # any valid id


class TestSauceJobs(unittest.TestCase):

    def setUp(self):
        self.jobs = SauceJobs(SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        if '' in (SAUCE_USERNAME, SAUCE_ACCESS_KEY, TEST_JOB_ID):
            raise SystemExit('Change your credentials (username/access-key)')

    def test_request(self):
        url = '/rest/v1/%s/jobs/%s' % (self.jobs.sauce_username, TEST_JOB_ID)
        json_data = self.jobs._request('GET', url)
        self.assertIsInstance(json_data, str)
        attributes = json.loads(json_data)
        self.assertIsInstance(attributes, dict)

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


if __name__ == '__main__':
    unittest.main(verbosity=2)
