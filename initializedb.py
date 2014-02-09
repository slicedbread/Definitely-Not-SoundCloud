import sqlite3


conn = sqlite3.connect('lyrics.db')
c = conn.cursor()
c.execute("CREATE TABLE songs(Title VARCHAR NOT NULL PRIMARY KEY, Artist VARCHAR, Year VARCHAR,  Lyrics VARCHAR)")  
if conn:
	conn.close()
