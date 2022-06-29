#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
<<<<<<< HEAD
    print(number, 'is positive')
elif number == 0:
    print(number, 'is zero')
else:
    print(number, 'is negative')
=======
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
>>>>>>> 86ee8188ca4eaa094b0e203b9f5b1de3c02b6277
