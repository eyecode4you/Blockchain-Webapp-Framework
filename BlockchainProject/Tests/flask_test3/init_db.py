#init_db.py - Use schema.sql to create initial db
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
	connection.executescript(f.read())
	
cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
				('First Post', 'Content for first post')
				)
				
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
			('Second Post', 'Content for second post')
			)

connection.commit()
connection.close()
