import sqlite3

conn = sqlite3.connect("sbinexus.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM profiles")

rows = cursor.fetchall()

print(rows)

conn.close()