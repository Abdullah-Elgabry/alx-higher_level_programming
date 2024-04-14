#!/usr/bin/python3
"""
script listing * states from hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This will Access to the db , featch the states from db
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
