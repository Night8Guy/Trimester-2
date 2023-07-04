#!/usr/bin/python3
"""
list all states with a name starting with N
from database hbtn_0e_0_USA
"""
import MySQLdb
import sys


def N_states():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY NAME LIKE 'N%' ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    N_states()