#!/usr/bin/python3
"""
Write a script that takes in arguments and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument. But this time,
    write one that is safe from MySQL injections!
"""
import MySQLdb
import sys


def list_states_by_name():
    """List the states specified safe from sql injection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    sql_com = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(sql_com, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states_by_name()