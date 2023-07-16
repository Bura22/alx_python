#!/usr/bin/python3
number = random.randint(-2147483648, 2147483647)

if number < 0:
    print(number, "is negative")
elif number > 0:
    print(number, "is positive")
else:
    print(number, "is zero")
