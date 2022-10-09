#/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that state, 
using the database hbtn_0e_4_usa
"""
import sys
import MySQL

if __name__ == "__main__":
  db = MySQL.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf-8")
  cur = db.cursor()
  cur.execute("SELECT c.name \
                 FROM cities AS c \
                      INNER JOIN states AS s \
                      ON c.state_id = s.id \
                 ORDER BY ASC c.id")
  rows = cur.fetchall()
  print(", ".join([ct[2] for row in rows if row[4] == sys.argv[4]]))
