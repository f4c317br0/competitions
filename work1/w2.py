import sqlite3

con = sqlite3.connect('districts.db')
cur = con.cursor()
a, b = input(), int(input())
result = cur.execute("""
SELECT tribute, score FROM Tributes
WHERE score >= ? AND district_id == (SELECT id FROM Districts WHERE district LIKE ?)
ORDER BY score DESC, tribute
""", (b, a)).fetchall()

for elem in result:
    print(f'{elem[0]} - {elem[1]} баллов')

con.close()
