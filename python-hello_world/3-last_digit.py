import random

number = random.randint(-100, 100)

lastDigit = number % 10

print("The last digit of {} is {}".format(number, lastDigit))
