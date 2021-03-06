from unittest2 import TestCase

from flask import url_for

from learnpython.app import app


class TestViews(TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

        self._ctx = app.test_request_context()
        self._ctx.push()

    def tearDown(self):
        self._ctx.pop()

    def test_index(self):
        index_url = url_for('index')
        response = self.client.get(index_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Learn Python', response.data)

    def test_static(self):
        url = url_for('static', filename='css/screen.css')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = url_for('static', filename='does_not_exists.exe')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
