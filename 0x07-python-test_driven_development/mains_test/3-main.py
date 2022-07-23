#!/usr/bin/python3
say_my_name = __import__("3-say_my_name").say_my_name

print(say_my_name("john", "Smith"))
print(say_my_name("Walter", "White"))
print(say_my_name("Bob"))
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
try:
    say_my_name("joe", 3)
except Exception as e:
    print(e)
