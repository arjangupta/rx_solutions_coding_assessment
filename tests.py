import unittest
from flask_testing import TestCase

from app import app

import json

class AllTests(TestCase):
    
    def create_app(self):
        return app
    
    def test_expected_request(self):
        encoded_json = json.dumps({'user_latitude':39.185811, 'user_longitude':-95.463779})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        expected_response = dict(pharmacy_name="HUNTERS RIDGE PHARMACY", \
                                 address="3405 NW HUNTERS RIDGE TER STE 200, TOPEKA, KS 66618", \
                                 distance=13.912812880008875)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_response)

    def test_latitude_out_of_range(self):
        encoded_json = json.dumps({'user_latitude':239.185811, 'user_longitude':-95.463779})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: latitude out of range. Must be within ' \
                                                 '[-90, 90]')

        encoded_json = json.dumps({'user_latitude':-4575.676776, 'user_longitude':-95.463779})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: latitude out of range. Must be within ' \
                                                 '[-90, 90]')

    def test_longitude_out_of_range(self):
        encoded_json = json.dumps({'user_latitude':-40.679, 'user_longitude':4759.999})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: longitude out of range. Must be within ' \
                                                 '[-180, 180]')

        encoded_json = json.dumps({'user_latitude':45.676776, 'user_longitude':-195.463779})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: longitude out of range. Must be within ' \
                                                 '[-180, 180]')

    def test_no_given_latitude(self):
        encoded_json = json.dumps({'user_longitude':-6.55554})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: request does not contain user\'s ' \
                                                 'latitude and longitude')

    def test_no_given_longitude(self):
        encoded_json = json.dumps({'user_latitude':-12312.55554})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: request does not contain user\'s ' \
                                                 'latitude and longitude')

    def irrelevant_json(self):
        encoded_json = json.dumps({'foo':'bar'})
        response = self.client.post('/api', data=encoded_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: request does not contain user\'s ' \
                                                 'latitude and longitude')

    def test_invalid_data_type(self):
        response = self.client.post('/api', data='Random text!')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Error: request is not JSON')
    
    def test_invalid_request_method(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 405)

        response = self.client.put('/api')
        self.assertEqual(response.status_code, 405)

        response = self.client.delete('/api')
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()