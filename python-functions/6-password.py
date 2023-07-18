#!/usr/bin/env python3

def validate_password(password):
        if any(char.isupper() for char in password) and len(password) >=8 and any(char.isupper() for char in password) and any(digit.isdigit() for digit in password) and not " " in password:
            return True
        return False

password  = input("Enter password: ")
checked = validate_password(password)

if checked == True:
      print("You can use this string as a password")
else:
      print("A string didn't match the requirement to be a password")

