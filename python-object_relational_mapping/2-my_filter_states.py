#!/usr/bin/python3
"""
script takes an argument and displays
all values in the states table from hbtn_0e_0_usa database
the names matche the argument
"""
import MySQLdb
import sys


def list_states_by_name():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
                 '{}' ORDER BY id".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_by_name()