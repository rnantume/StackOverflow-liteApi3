from flask import Flask, Blueprint

from API.resources.users import users_bp
from API.resources.questions import questions_bp

app = Flask(__name__,instance_relative_config=True)
app.config['DEBUG'] = True


"""
registering the users, questions blueprint
"""
app.register_blueprint(users_bp)
# app.register_blueprint(questions_bp)

