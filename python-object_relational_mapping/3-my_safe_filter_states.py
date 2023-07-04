#!/usr/bin/python3
"""
script that takes arguments and displays all values in states table
hbtn_0e_0_usa datbase where name matches argument
"""
import MySQLdb
import sys


def list_states_by_name_again():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    buffer_string = "SELECT * FROM states WHERE name = %s ORDER BY id"
    
    cursor.execute(buffer_string, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_by_name_again()