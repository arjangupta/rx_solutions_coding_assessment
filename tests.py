import unittest
from flask_testing import TestCase

from app import app

import json

class AllTests(TestCase):
    
    def create_app(self):
        return app
    
    def test_expected_request(self):
        encoded_json = json.dumps({'latitude':45.674, 'longitude':100.234})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, json.loads(encoded_json))
    
    def test_invalid_request_method(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 405)

        response = self.client.put('/api')
        self.assertEqual(response.status_code, 405)

        response = self.client.delete('/api')
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()