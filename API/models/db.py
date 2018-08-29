import psycopg2
import datetime

from config import config

def connection():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            userId SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL, 
            email VARCHAR(255),
            password VARCHAR(255)
            )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS questions (
            userId INTEGER,
            questionId SERIAL PRIMARY KEY,
            Topic VARCHAR(255) NOT NULL,
            Description VARCHAR(255),
            created_at VARCHAR(255),
            FOREIGN KEY(userId)
            REFERENCES users(userId)
            )
        """,
        """
        CREATE TABLE IF NOT EXISTS answers(
            questionId INTEGER,
            userId INTEGER,
            answerId SERIAL PRIMARY KEY,
            answer VARCHAR(255) NOT NULL,
            created_at VARCHAR(255),
            FOREIGN KEY (questionId)
            REFERENCES questions (questionId)
            ON UPDATE CASCADE ON DELETE CASCADE
            )
        """
        )
    connection = None
    try:
        # read the connection parameters
        params = config()

        # connect to the PostgreSQL server
        connection = psycopg2.connect(**params)
        connection.autocommit = True
        cursor = connection.cursor()

        # create table one by one
        for command in commands:
            cursor.execute(command)
        return cursor

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
