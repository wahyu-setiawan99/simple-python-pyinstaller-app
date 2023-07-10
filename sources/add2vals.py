'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

print("Please insert the first number:")


x = input()
first_number = str(x).strip()

print("Please insert the second number:")
y = input()
second_number = str(y).strip()

argnumbers = len(first_number.split()) + len(second_number.split())

if argnumbers == 2 :
    print("")
    print("The result is " + str(calc.add2(first_number, second_number)))
    print("")
    sys.exit(0)


if argnumbers != 2 :
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: run add2valsand and insert the first and second number without space.")
    print("       If add2vals is not in your path, usage is './add2vals'.")
    print("       If unbundled, usage is 'python add2vals.py'.")
    print("")
    sys.exit(1)
