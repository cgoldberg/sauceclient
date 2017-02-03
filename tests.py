import unittest

import sauceclient

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


@patch('sauceclient.http_client.HTTPSConnection.getresponse')
class TestSauce(unittest.TestCase):

    def setUp(self):
        self.sc = sauceclient.SauceClient('sauce-username', 'sauce-access-key')

    def test_bad_request(self, mocked):
        mocked.return_value.status = 400
        mocked.return_value.reason = 'BAD'

        self.assertRaises(sauceclient.SauceException,
                          self.sc.information.get_status)

    def test_account_get_user(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.account.get_user()
        self.assertIsInstance(resp, dict)

    def test_account_create_user(self, mocked):
        mocked.return_value.status = 201
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.account.create_user('username', 'password', 'Full Name',
                                           'email@example.com')
        self.assertIsInstance(resp, dict)

    def test_account_get_concurrency(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.account.get_concurrency()
        self.assertIsInstance(resp, dict)

    def test_account_get_subaccounts(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.account.get_subaccounts()
        self.assertIsInstance(resp, dict)

    def test_account_get_siblings(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'[]'

        resp = self.sc.account.get_siblings()
        self.assertIsInstance(resp, list)

    def test_account_get_subaccount_info(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'[]'

        resp = self.sc.account.get_subaccount_info()
        self.assertIsInstance(resp, list)

    def test_account_change_access_key(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.account.change_access_key()
        self.assertIsInstance(resp, dict)

    def test_account_get_activity(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.account.get_activity()
        self.assertIsInstance(resp, dict)

    def test_account_get_usage(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.account.get_usage()
        self.assertIsInstance(resp, dict)

        resp = self.sc.account.get_usage(start='1976-10-23', end='1976-10-23')
        self.assertIsInstance(resp, dict)

    """INFORMATION"""
    def test_information_get_status(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.information.get_status()
        self.assertIsInstance(resp, dict)

    def test_information_get_platforms(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'[]'

        resp = self.sc.information.get_platforms()
        self.assertIsInstance(resp, list)

        resp = self.sc.information.get_platforms('webdriver')
        self.assertIsInstance(resp, list)

        resp = self.sc.information.get_platforms('appium')
        self.assertIsInstance(resp, list)

    def test_information_get_appium_eol_dates(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.information.get_appium_eol_dates()
        self.assertIsInstance(resp, dict)

    def test_javascript_js_tests(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.javascript.js_tests(
                                            ['OS X 10.11', 'chrome', ''],
                                            'http://example.com/',
                                            'jasmine')
        self.assertIsInstance(resp, dict)

    def test_javascript_js_tests_status(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.javascript.js_tests_status(['test-1', 'test-2'])
        self.assertIsInstance(resp, dict)

    def test_jobs_get_jobs(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'[]'

        resp = self.sc.jobs.get_jobs()
        self.assertIsInstance(resp, list)

        resp = self.sc.jobs.get_jobs(full=True, limit=1, skip=1,
                                     start=214891200, end=214975439,
                                     output_format='json')
        self.assertIsInstance(resp, list)

    def test_jobs_get_job(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.jobs.get_job('job-id')
        self.assertIsInstance(resp, dict)

    def test_jobs_update_job(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.jobs.update_job('job-id', build=1, custom_data={},
                                       name='Name', passed=True,
                                       public='private', tags=[])
        self.assertIsInstance(resp, dict)

    def test_jobs_delete_job(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.jobs.delete_job('job-id')
        self.assertIsInstance(resp, dict)

    def test_jobs_stop_job(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.jobs.stop_job('job-id')
        self.assertIsInstance(resp, dict)

    def test_jobs_get_job_assets(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.jobs.get_job_assets('job-id')
        self.assertIsInstance(resp, dict)

    def test_jobs_get_job_asset_url(self, mocked):
        resp = self.sc.jobs.get_job_asset_url('job-id', '0000screenshot.jpg')
        self.assertIsInstance(resp, str)

    def test_jobs_delete_job_assets(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'[]'

        resp = self.sc.jobs.delete_job_assets('job-id')
        self.assertIsInstance(resp, list)

    def test_jobs_get_auth_token(self, mocked):
        resp = self.sc.jobs.get_auth_token('job-id')
        self.assertIsInstance(resp, str)

        resp = self.sc.jobs.get_auth_token('job-id', '1976-10-23')
        self.assertIsInstance(resp, str)

    def test_storage_upload_file(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.storage.upload_file('./README.rst')
        self.assertIsInstance(resp, dict)

    def test_storage_get_stored_files(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.storage.get_stored_files()
        self.assertIsInstance(resp, dict)

    def test_tunnels_get_tunnels(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'[]'

        resp = self.sc.tunnels.get_tunnels()
        self.assertIsInstance(resp, list)

    def test_tunnels_get_tunnel(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.tunnels.get_tunnel('tunnel-id')
        self.assertIsInstance(resp, dict)

    def test_storage_delete_tunnel(self, mocked):
        mocked.return_value.status = 200
        mocked.return_value.reason = 'OK'
        mocked.return_value.read.return_value = b'{}'

        resp = self.sc.tunnels.delete_tunnel('tunnel-id')
        self.assertIsInstance(resp, dict)


if __name__ == '__main__':
    unittest.main()
