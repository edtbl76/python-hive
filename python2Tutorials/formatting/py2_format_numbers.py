#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function

def main():

    # Old
    print('%d' % 42)
    print('%+d' % 42)                   # adds + sign
    print('% d' % -42)                  # (adds a space to hold the negative sign)
    print('|%4d' % 42, end="|\n")       # w/ Padding (auto justify right)
    print('|%04d' % 42, end="|\n")      # w/ Padding (auto justify right) and 0 fill
    print('%f' % 3.141592653589793)     # w/ float
    print('%.2f' % 3.141592653589793)   # w/ float and precision
    print('|%5.2f' % 3.141592653589793, end="|\n")     # w/ float, precision and padding.
    print('|%05.2f' % 3.141592653589793, end="|\n")     # w/ float, precision, padding and zero fill

    print()

    # New
    print("{}".format(42))
    print("{:+d}".format(42))                   # adds + sign
    print("{:+=5d}".format(42))                 # control position of positive sign.
    print("{: d}".format(-42))                  # adds space to hold the negative sign.
    print("{:=5d}".format(-42))                 # control position of negative sign
    print("|{:4d}".format(42), end="|\n")       # w/ padding (auto justify right)
    print("|{:04d}".format(42), end="|\n")      # w/ padding (auto justify right) &b 0 fill.
    print("{:f}".format(3.141592653589793))     # w/ float
    print("{:.2f}".format(3.141592653589793))     # w/ float and precision
    print("|{:5.2f}".format(3.141592653589793), end="|\n")     # w/ float, precision and padding.
    print("|{:05.2f}".format(3.141592653589793), end="|\n")     # w/ float, precision, padding and zero fill


if __name__ == '__main__':
    main()
