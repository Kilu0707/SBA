import sqlite3
 
conn = sqlite3.connect('5A23 Fan Hau Ki_SBA.db')
cursor = conn.cursor()
 
cursor.execute("SELECT * FROM Room")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()