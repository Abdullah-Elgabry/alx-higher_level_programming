#!/usr/bin/python3
"""
script show the states by name st with ' N' letter
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
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
