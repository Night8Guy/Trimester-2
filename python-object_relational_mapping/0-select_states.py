#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states():
    """
    Connect to MySQL server
    REMEMBER! the username, password, and db are passed as arguments!
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """
    Create a cursor object to execute SQL queries
    note: the cursor object allows the 'cursor.execute' line below
    to execute what the text says like its SQL
    """
    cursor = db.cursor()

    """Execute a query to fetch all states"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all the rows returned by the query"""
    rows = cursor.fetchall()

    """Display the results"""
    for row in rows:
        print(row)

    """
    Close the cursor and database connection
    THIS IS GOOD PRACTICE
    """
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()