import sqlite3

con = sqlite3.connect('sample.db')
cur = con.cursor()

result = cur.execute("""
SELECT tribute, district, score FROM Tributes
""").fetchall()

for elem in result:
    print(elem[0], elem[1], elem[2])

con.close()