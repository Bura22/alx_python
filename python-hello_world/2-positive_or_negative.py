#!/usr/bin/python3

import random

number = random.randint(-100, 100)
num = number - 10//2

if num < 0:
    print(num, "is negative")
elif number > 0:
    print(num, "is positive")
else:
    print(num, "is zero")
