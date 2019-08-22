import unittest
from flask_testing import TestCase

from app import app

class AllTests(TestCase):
    
    def create_app(self):
        return app
    
    def test_invalid_request_method(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 405)

        response = self.client.put('/api')
        self.assertEqual(response.status_code, 405)

        response = self.client.delete('/api')
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()