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
        

    def test_api_gets_all_qns(self):
        """Test API can get all questions in the database"""
        res = self.client.get('/StackOverflow-lite/api/v1/questions')
        self.assertEqual(res.status_code, 200)

    

    def tearDown(self):
        """teardown initialised variables"""
        pass

if __name__ =='__main__':
    unittest.main()
