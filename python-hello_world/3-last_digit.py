number = random.randint(-10000, 10000)

if number < 0:
    new = number * -1
    lastDigit = new % 10
else:
    new = number
    lastDigit = new % 10

print(number, lastDigit)
if lastDigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastDigit))
else:
    print("Last digit of {} is {} and is less than 5".format(number, lastDigit))

