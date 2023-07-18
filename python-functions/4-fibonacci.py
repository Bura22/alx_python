#!/usr/bin/env python3

def fibonacci_sequence(n):
    a, b = 0, 1
    c = 0
    for i in range(0, n):
        print(c, end=" ")
        a = b
        b = c
        c = a + b
number  = int(input("Enter number: "))
fibonacci_sequence(number)