#!/usr/bin/python3
"""
script prints all states in db
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This will Access to the db , featch the states from db
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
