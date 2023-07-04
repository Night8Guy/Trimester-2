#!/usr/bin/python3
"""
script that takes name of a state
as argument and lists all cities in that state
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities_by_state():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    buffer_string = "SELECT cities.name FROM cities\
                JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s ORDER BY cities.id ASC"

    cursor.execute(buffer_string, (sys.argv[4],))

    rows = cursor.fetchall()

    """
    Must Print Again
    """
    if len(rows) == 0:
        print()
        return

    for i in range(len(rows) - 1):
        print(rows[i][0], end=', ')
    print(rows[len(rows) - 1][0])

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()