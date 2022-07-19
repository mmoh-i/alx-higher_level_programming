#!/bin/usr/python3
def safe_print_integer_err(value):
    try:
        print("{}".format(value)
        return True
    except (TypeError, ValueError) as tv:
        print("Exception: {}".format(tv), file=sys.stderr)
        return False
