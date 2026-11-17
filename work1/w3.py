import sqlite3


def battle_report(district='Все', points=0):
    con = sqlite3.connect('arena.db')
    cur = con.cursor()

    cur.execute("DELETE FROM Results")

    cur.execute("""
        INSERT INTO Results (no, tribute, place, points)
        SELECT
            ROW_NUMBER() OVER (ORDER BY b.id),
            t.tribute,
            b.place,
            b.points
        FROM Battles AS b
        JOIN Tributes AS t ON b.tribute_id = t.id
        JOIN Districts AS d ON t.district_id = d.id
        WHERE
            (:district = 'Все' OR d.district = :district)
            AND b.points >= :points
        ORDER BY b.id
    """, {'district': district, 'points': points})

    con.commit()
    con.close()


if __name__ == '__main__':
    battle_report('Дистрикт 3', 31)
