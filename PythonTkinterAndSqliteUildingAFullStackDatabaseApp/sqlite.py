import sqlite3
database_path = 'PythonTkinterAndSqliteUildingAFullStackDatabaseApp\school.db'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()
sql = ('''CREATE TABLE IF NOT EXISTS companies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)''')
cursor.execute(sql)
sql = ('''CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, category TEXT NOT NULL, company_id INTEGER)''')
cursor.execute(sql)