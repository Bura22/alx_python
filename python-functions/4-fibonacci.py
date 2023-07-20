#!/usr/bin/env python3

def fibonacci_sequence(n):
    a = 0
    b = 1
    series =[]
    series.append(a)
    series.append(b)
    while (n > 0):
        allTotal = a + b
        series.append(allTotal)
        a = b
        b = allTotal
        n -=1
    return series