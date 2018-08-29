import datetime

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
        result = connection().execute(query, (username,))
        row = result.fetchone()
        if row:
            user =  cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_userId(cls, userId):
        query = """SELECT * FROM users WHERE userId =%s"""
        result = connection().execute(query, (userId,))
        row = result.fetchone()
        if row:
            user =  cls(*row)
        else:
            user = None

        connection.close()
        return user

class Question:
    
    @staticmethod
    def get_questions():
        """
        gets all questions in database and returns list of questions"""
        cursor = connection()
        query = """SELECT * FROM questions"""
        result = cursor.execute(query)
        questions = result.fetchall()

        keys = ["userId", "questionId", ]
        def dictify(qtn):
            return dict(zip(keys, questions))

        qtns = [dictify(qtn) for qtn in questions]
        return qtns