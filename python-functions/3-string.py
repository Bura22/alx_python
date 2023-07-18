#!/usr/bin/env python3
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

string = input("Enter a string: ")
print("THe reversed form of {} is {}".format(string, reverse_string(string)))