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
                            'password':'G@mb13rs', 'verify_password':'G@mb13rs'}
        self.user = {'username':'robin','password':'G@mb13rs'}
        self.with_unknown_username = {'username':'wrong','password':'G@mb13rs'}
        self.with_wrong_pass = {'username':'unknown','password':'wrong'}

    def test_api_logs_in_valid_user(self):
        """Test API can sign up a new user(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        """Test API can login a registered user(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/login',
                         data=json.dumps(self.user),content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_api_doesnot_login_with_unknown_username(self):
        """Test API can sign up a new user(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        """Test API can login a registered user
            who entere wrong username on login(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/login',
                         data=json.dumps(self.with_unknown_username),content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_api_doesnot_login_with_wrong_password(self):
        """Test API can sign up a new user(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        """Test API can login a registered user
            who enters wrong password on login(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/login',
                         data=json.dumps(self.with_wrong_pass),content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def tearDown(self):
        """teardown table contents"""
        query = """DROP TABLE users CASCADE"""
        cur = connection()
        cur.execute(query)

if __name__ =='__main__':
    unittest.main()
