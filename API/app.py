from flask import Flask, Blueprint


app = Flask(__name__,instance_relative_config=True)

app.config['DEBUG'] = True

from API.resources.users import users_bp

"""
registering the users blueprint
"""
app.register_blueprint(users_bp)


