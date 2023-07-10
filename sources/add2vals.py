'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

print("Please insert the first number:")
x = str(input())
first_number = x.strip()

print("Please insert the second number:")
y = str(input())
second_number = y.strip()

argnumbers = len(first_number.split()) + len(second_number.split())

if argnumbers == 2 :
    print("")
    print("The result is " + str(calc.add2(first_number, second_number)))
    print("")
    sys.exit(0)
