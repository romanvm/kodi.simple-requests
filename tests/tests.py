import io
import pickle
import sys
from pathlib import Path
from unittest import TestCase, main as unittest_main

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / 'script.module.simple-requests' / 'libs'))

import simple_requests as requests

BASE_URL = 'https://httpbin.org'


class GetTestCase(TestCase):

    @staticmethod
    def _call_url(*args, **kwargs):
        response = requests.get(*args, **kwargs)
        return response

    def test_simple_get(self):
        response = self._call_url(BASE_URL + '/html', headers={'Accept': 'text/html'})
        self.assertTrue(response.ok)
        self.assertIn('Herman Melville - Moby-Dick', response.text)

    def test_simple_get_http(self):
        response = self._call_url('http://httpbin.org/html', headers={'Accept': 'text/html'})
        self.assertTrue(response.ok)
        self.assertIn('Herman Melville - Moby-Dick', response.text)

    def test_get_json(self):
        response = self._call_url(BASE_URL + '/json', headers={'Accept': 'application/json'})
        self.assertIn('slideshow', response.json())

    def test_get_params(self):
        response = self._call_url(BASE_URL + '/get', params={'foo': 'bar'})
        self.assertEqual(response.json()['args']['foo'], 'bar')

    def test_headers(self):
        response = self._call_url(BASE_URL + '/get', headers={'X-Foo': 'bar'})
        self.assertEqual(response.json()['headers']['X-Foo'], 'bar')

    def test_set_cookies_from_dict(self):
        response = self._call_url(BASE_URL + '/cookies/set', params={'foo': 'bar'})
        self.assertEqual(response.json()['cookies']['foo'], 'bar')

    def test_basic_auth(self):
        response = self._call_url(BASE_URL + '/basic-auth/foo/bar', auth=('foo', 'bar'))
        self.assertTrue(response.ok)
        self.assertEqual(response.json()['user'], 'foo')

    def test_gzipped_response_content(self):
        response = self._call_url(BASE_URL + '/gzip')
        self.assertTrue(response.json()['gzipped'])

    def test_response_cookies(self):
        response = self._call_url('https://google.com', headers={'Accept': 'text/html'})
        self.assertIn('AEC', response.cookies)

    def test_get_error_400(self):
        response = self._call_url(BASE_URL + '/status/400')
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.ok)
        self.assertRaises(requests.HTTPError, response.raise_for_status)


class PostTestCase(TestCase):

    @staticmethod
    def _call_url(*args, **kwargs):
        response = requests.post(*args, **kwargs)
        return response

    def test_json_payload(self):
        payload = {'foo': 'bar'}
        response = self._call_url(BASE_URL + '/post', json=payload)
        self.assertEqual(response.json()['json'], payload)

    def test_form_data_payload(self):
        payload = {'foo': 'bar'}
        response = self._call_url(BASE_URL + '/post', data={'foo': 'bar'})
        self.assertEqual(response.json()['form'], payload)

    def test_bytes_payload(self):
        payload = b'foo'
        response = self._call_url(BASE_URL + '/post', data=payload)
        self.assertEqual(response.json()['data'], payload.decode('utf-8'))

    def test_str_payload(self):
        payload = 'foo'
        response = self._call_url(BASE_URL + '/post', data=payload)
        self.assertEqual(response.json()['data'], payload)

    def test_fileobj_payload(self):
        payload = io.BytesIO(b'foo')
        response = self._call_url(BASE_URL + '/post', data=payload)
        self.assertEqual(response.json()['data'], 'foo')


class RequestsCookieJarTestCase(TestCase):

    def test_pickling_and_unpickling(self):
        cookie_jar = requests.RequestsCookieJar()
        cookie_jar['foo'] = 'bar'
        picked_bytes = pickle.dumps(cookie_jar)
        unpickled_cookie_jar = pickle.loads(picked_bytes)
        self.assertEqual(unpickled_cookie_jar['foo'], 'bar')


if __name__ == '__main__':
    unittest_main()
