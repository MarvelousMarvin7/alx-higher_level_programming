#!/usr/bin/python3
""" List all states from database """

import MySQLdb
import sys

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host='localhost', user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()
