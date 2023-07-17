import random

number = random.randint(-100, 100)

lastDigit = number % 10

if lastDigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastDigit))
else:
    print("Last digit of {} is {} and is less than 5".format(number, lastDigit))

