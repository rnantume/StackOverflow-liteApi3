from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager

from API.resources.users import users_bp
from API.resources.questions import questions_bp
from API.resources.answers import answers_bp

app = Flask(__name__,instance_relative_config=True)
app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)


"""
registering the users, questions, answers blueprints
"""
app.register_blueprint(users_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(answers_bp)