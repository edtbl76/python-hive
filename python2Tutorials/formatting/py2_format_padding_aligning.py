#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function

def main():

    # Align Right
    print('|%10s' % 'test', end="|\n")          # Old
    print("|{:>10}".format('test'), end="|\n")  # New
    print("|{:->10}".format('test'), end="|\n") # New w/ padding.


    # Align Left
    print('|%-10s' % 'test', end="|\n")         # Old
    # Note that the < character is only required when using padding, as left
    # alignment is default in the new formatting style.
    print("|{:10}".format('test'), end="|\n")   # New
    print("|{:-<10}".format('test'), end="|\n") # New w/ padding.

    # Center (New Only)
    print("|{:^10}".format('test'), end="|\n")
    print("|{:-^10}".format('test'), end="|\n") # w/ padding.
    print("|{:-^9}".format('test'), end="|\n")  # w/ uneven padding.


if __name__ == '__main__':
    main()
