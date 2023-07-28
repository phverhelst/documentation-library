import sqlite3

def connect():
    connection = sqlite3.connect("PythonTkinterAndSqliteUildingAFullStackDatabaseApp/courses.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS course(
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        author TEXT,
        price TEXT)
        ''')

    connection.commit()
    connection.close()

def create(name, category, author, price):
    connection = sqlite3.connect("PythonTkinterAndSqliteUildingAFullStackDatabaseApp/courses.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course VALUES (NULL, ?, ?, ?, ?)",  (name, category, author, price))
    connection.commit()
    connection.close()

def read_all():
    connection = sqlite3.connect("PythonTkinterAndSqliteUildingAFullStackDatabaseApp/courses.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

