import mysql.connector as mysql


def connect():

    return mysql.connect(
        host="localhost",
        user="root",
        password="1111",
        database='kivy_practice'
    )
