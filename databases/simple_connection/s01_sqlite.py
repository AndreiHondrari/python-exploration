#!python3


import sqlite3

conn = sqlite3.connect("some.db")

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS bla (x integer)")
c.execute("INSERT INTO bla VALUES (10)")
c.execute("INSERT INTO bla VALUES (20)")
c.execute("INSERT INTO bla VALUES (30)")
c.execute("INSERT INTO bla VALUES (40)")

conn.commit()
conn.close()
