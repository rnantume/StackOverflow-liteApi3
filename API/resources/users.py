"""contains various routes for the users endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, fields, inputs, Api,
                            marshal)

from API.models.allmodels import User

class Signup(Resource):
    """
    Lets one POST to add new account
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, 
                            nullable=False, help="username cannot be null or none",
                            location = ['form', 'json'], trim=True
                            )
        self.reqparse.add_argument('email', type=str, required=True, 
                            nullable=False, help="email cannot be null or none",
                            location = ['form', 'json'], trim=True
                            )
        self.reqparse.add_argument('password', type=str, required=True, 
                            nullable=False, help="password cannot be null or none",
                            location = ['form', 'json']
                            )
        super().__init__()

    def post(self):
        """
        create a new user
        """
        args = self.reqparse.parse_args()
        new_user = User(**args).signup_users()
        return {'message':'You have successfully signed up with StackOverflow-lite'},201

users_bp = Blueprint('api_logic.users', __name__)
users_api = Api(users_bp)

users_api.add_resource(Signup,
    '/StackOverflow-lite/api/v1/auth/signup',
    endpoint='signup')