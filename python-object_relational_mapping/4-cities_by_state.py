#!/usr/bin/python3
"""
script that lists all cities from database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities():
    """List the cities"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states ON states.id\
                = cities.state_id ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()