import psycopg2
import datetime

from config import config

def create_tables():
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
            questionId SERIAL PRIMARY KEY,
            Topic VARCHAR(255) NOT NULL,
            Description (255),
            created_at VARCHAR(255),
            FOREIGN KEY(userId)
            REFERENCES users(userId)
            )
        """,
        """
        CREATE TABLE IF NOT EXISTS answers(
            answerId INTEGER PRIMARY KEY,
            answer VARCHAR(255) NOT NULL,
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
        print(params)
        # connect to the PostgreSQL server
        # connection = psycopg2.connect(**params)
        connection = psycopg2.connect(host=params['post'], dbname=params['database'], user=params['user'], password=params['password'])
        cursor = connection.cursor()

        # create table one by one
        for command in commands:
            cursor.execute(command)

        # close communication with the PostgreSQL database server
        cursor.close()

        # commit the changes
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Cannot connect to database")
    else:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


