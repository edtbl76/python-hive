#!/usr/bin/env python
from __future__ import print_function

def main():

    # Entire Statement
    print("Hello, World")

    # Using the 'end' argument
    print("Hello,", end=" World\n")

    # Using a variable
    msg = "Hello, World"
    print(msg)

    # Using Python's internal space separator
    print("Hello,", "World")

    # Adjusting the separator
    print("Hello", "World", sep=", ")

if __name__ == '__main__':
    main()
