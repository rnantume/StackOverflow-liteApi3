from flask import Flask, Blueprint
from flask_jwt import JWT


from API.resources.auth import authenticate, identity
from API.resources.users import users_bp
# from API.resources.questions import questions_bp

app = Flask(__name__,instance_relative_config=True)
app.secret_key = 'qwertyrvtimber'
app.config['DEBUG'] = True

jwt = JWT(app, authenticate, identity) #creates a default route /auth


"""
registering the users, questions blueprint
"""
app.register_blueprint(users_bp)
# app.register_blueprint(questions_bp)

