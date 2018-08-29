from .db import connection


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def signup_users(self):
        insert_user = """INSERT INTO users(username, email, password) VALUES (%s, %s, %s)"""
        connection().execute(insert_user, (self.username, self.email, self.password))
