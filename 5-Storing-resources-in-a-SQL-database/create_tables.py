import sqlite3

DB_FILE = "data.db"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

connection.commit()
connection.close()
