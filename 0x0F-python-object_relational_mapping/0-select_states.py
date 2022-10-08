#!/usr/bin/python3
"""
Script should take three arguments: mysql usernae
mysql password, dataase name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQL.connect(user=sys.argv[1], passwd=sys.agv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
