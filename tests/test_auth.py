import unittest
import json

from API.app import app
from API.models.db import connection

class UsersTestCase(unittest.TestCase):
    """class to represent users and authentication test case"""

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        
        """setup test variables"""
        self.new_user = {'username':'robin','email':'nnrobin37@gmail.com',
                            'password':'der1234'}

    def test_api_adds_new_user(self):
        """Test API can add new user to database(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)

    

    def tearDown(self):
        """teardown initialised variables"""
        pass

if __name__ =='__main__':
    unittest.main()
