import sqlite3

conn = sqlite3.connect('site.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(15) not null,
    email varchar(25) not null
)               
''')

conn.commit()
conn.close()