#!/usr/bin/python3
""" List all states from database with name starting with N """

import MySQLdb
import sys

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host='localhost', user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db_conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()
