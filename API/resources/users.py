"""contains various routes for the users endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, fields, inputs, Api,
                            marshal)
from flask_jwt_extended import create_access_token

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
        self.reqparse.add_argument('email',
                            type=inputs.regex('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),
                            required=True, 
                            nullable=False, help="Wrong email address",
                            location = ['form', 'json'], trim=True
                            )
        self.reqparse.add_argument('password', 
                            type=inputs.regex('^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=.]).*$'),
                            required=True, nullable=False,
                            help="Password must atleast contain 8 alphanumerical characters, atleast 1 uppercase or lowercase letters and any 1 of special characters",
                            location = ['form', 'json']
                            )
        self.reqparse.add_argument('verify_password',
                            required=True, nullable=False, help="No password verification provided",
                            location = ['form', 'json']
                            )
        super().__init__()

    def post(self):
        """
        create a new user
        """
        args = self.reqparse.parse_args()
        if args.get('password') != args.get('verify_password'):
            return {"message":"password and password verification do not match"},400
        if User.find_by_username(args['username']):
            return {"message":"A user with that username already exist"}, 400
        if User.find_by_email(args['email']):
            return {"message":"A user with that email already exist"}, 400
        else:
            new_user = User(args['username'],args['email'],args['password']).signup_users()
            return {'message':'You have successfully signed up with StackOverflow-lite'},201

class Login(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, 
                            nullable=False, help="username cannot be null or none",
                            location = ['form', 'json'], trim=True
                            )
        self.reqparse.add_argument('password',
                            required=True, nullable=False, help="password cannot be null or none",
                            location = ['form', 'json'])
        super().__init__()

    def post(self):
        """
        logging in a user
        """
        args = self.reqparse.parse_args()
        user = User(args['username'], None, args['password'])
        logging_user = user.signin_user(args['username'])

        if logging_user  is not None:
            token = create_access_token(identity=args['username'])
            return jsonify({"token":token}),200
        else:
            return jsonify({"message":"Login failed!"}), 400



users_bp = Blueprint('api_logic.users', __name__)
users_api = Api(users_bp)

users_api.add_resource(Signup,
    '/StackOverflow-lite/api/v1/auth/signup',
    endpoint='signup')

users_api.add_resource(Signup,
    '/StackOverflow-lite/api/v1/auth/login',
    endpoint='login')