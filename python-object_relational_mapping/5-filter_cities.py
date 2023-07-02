#!/usr/bin/python3
"""
Write a script that takes in the name of a state
    as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities_by_state():
    """List the cities of a state"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    sql_com = "SELECT cities.name FROM cities JOIN states\
                ON states.id = cities.state_id WHERE states.name\
                = %s ORDER BY cities.id"
    cur.execute(sql_com, (sys.argv[4],))

    rows = cur.fetchall()

    if len(rows) == 0:
        print()
        return

    for i in range(len(rows) - 1):
        print(rows[i][0], end=', ')
    print(rows[len(rows) - 1][0])

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()