from flask import jsonify
import re

from .db import connection


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def signup_users(self):
        insert_user = """INSERT INTO users(username, email, password) VALUES (%s, %s, %s)"""
        connection().execute(insert_user, (self.username, self.email, self.password))

    @classmethod
    def find_by_username(cls, username):
        query = """SELECT * FROM users WHERE username =%s"""
        cur = connection()
        cur.execute(query, (username,))
        row = cur.fetchone()
        if row:
            return row
        else:
            user = None

    @classmethod
    def find_by_email(cls, email):
        query = """SELECT * FROM users WHERE email =%s"""
        cur = connection()
        cur.execute(query, (email,))
        row = cur.fetchone()
        if row:
            return row
        else:
            user = None

    @classmethod
    def find_by_userId(cls, userId):
        query = """SELECT * FROM users WHERE userId =%s"""
        cur = connection()
        cur.execute(query, (userId,))
        row = result.fetchone()
        if row:
            return row[0]
        else:
            return None
        
    @classmethod
    def signin_user(cls, username, password):
        user = User.find_by_username(username)
        pass_ = user[3]
        if user and pass_==password:
            return user

    @staticmethod
    def identity(payload):
        userId = payload['identity']
        return User.find_by_userId(userId)

class Question:

    @staticmethod
    def get_questions():
        """
        gets all questions in database and returns list of questions
        """
        query = """SELECT * FROM questions"""
        cur = connection()
        cur.execute(query)
        questions = cur.fetchall()

        keys = ["userId", "questionId", "Topic", "Description", "created_at"]
        def dictify(qtn):
            return dict(zip(keys, qtn))

        qtns = [dictify(qtn) for qtn in questions]
        return qtns
