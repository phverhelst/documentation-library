import sqlite3

def connect():

    connection = sqlite3.connect("courses.db")
    cursor = connection.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS course
                   (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   category TEXT
                   )
                   '''
    )

    connection.commit()
    connection.close()

connect()