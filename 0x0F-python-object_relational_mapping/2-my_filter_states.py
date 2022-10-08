#!/usr/bin/python3
"""
Scriit that takes inan argument and displays
all th value in the states table fo hbtn_0e_p0_usa
where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQL.connect(user=sys.argv[1], port=3306, host="localhost",
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.exceute("SELECT * FROM states  WHERE name LIKE '{:s}' ORDER BY\
            ID ASC".format(sys.argv[4]))
    states = c.fetchall()
    for states in states:
        if states[1] ==  sys.argv[4]:
            print(state)
    c.close()
    db.close()
