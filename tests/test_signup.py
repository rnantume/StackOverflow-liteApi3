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
        self.another_user = {'username':'stella','email':'calyphstruck@gmail.com',
                            'password':'G@mb13rs', 'verify_password':'G@mb13rs'}
        self.with_wrong_email = {'username':'robin','email':'robin',
                            'password':'G@mb13rs', 'verify_password':'G@mb13rs'}
        self.with_wrong_password = {'username':'robin','email':'nnrobin37@gmail.com',
                            'password':'1234', 'verify_password':'1234'}
        self.with_no_match = {'username':'robin','email':'nnrobin37@gmail.com',
                            'password':'G@mb13rs', 'verify_password':'1234'}                            

    def test_api_adds_new_user(self):
        """Test API can add new user to database(POST request)."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        
    def test_api_cannot_add_user_with_wrong_email(self):
        """Test API cannot add new user to database(POST request) if email is invalid."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.with_wrong_email),content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_api_cannot_post_user_if_password_is_wrong(self):
        """Test API cannot add new user to database(POST request) if password is wrong."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.with_wrong_password),content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_api_cannot_post_user_if_password_and_verification_dont_match(self):
        """Test API cannot add new user to database(POST request) if password 
            and verify_password do not match"""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                          data=json.dumps(self.with_no_match),content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_api_cannot_post_user_if_username_already_exists(self):
        """Test API cannot add new user to database(POST request) if password is wrong."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_api_cannot_post_user_if_email_already_exists(self):
        """Test API cannot add new user to database(POST request) if password is wrong."""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_api_posts_user_with_different_credentila(self):
        """Test API now posts new user with different credentila"""
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.new_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client.post('/StackOverflow-lite/api/v1/auth/signup',
                         data=json.dumps(self.another_user),content_type='application/json')
        self.assertEqual(res.status_code, 201)


    def tearDown(self):
        """teardown table contents"""
        query = """DROP TABLE users CASCADE"""
        cur = connection()
        cur.execute(query)

if __name__ =='__main__':
    unittest.main()
