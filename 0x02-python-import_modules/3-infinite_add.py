#!/usr/bin/python
import sys
if __name__ == "__main__":
    from sys import argv
   # l = len(argv)
    add = 0
    for i in argv[1:]:
        add += int(i)
    print("{:d}".format(add)) 
