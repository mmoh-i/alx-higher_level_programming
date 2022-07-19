#!/bin/usr/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        return None
    return result
