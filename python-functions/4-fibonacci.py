#!/usr/bin/env python3

def fibonacci_sequence(n):
    a = 0
    b = 1
    series = []
    if n == 1:
        series.append(a)
    if n >= 2:
        series.append(a)
        series.append(b)
    if n == 2:
        series.append(a)
        series.append(b)
    while (n > 2):
        allTotal = a + b
        series.append(allTotal)
        a = b
        b = allTotal
        n -=1
    return series
