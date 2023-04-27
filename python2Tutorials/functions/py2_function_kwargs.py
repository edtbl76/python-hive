#!/usr/bin/env python
from __future__ import print_function

def abcd(a, b, c=0, d=0):
    """ 2 positional args, and 2 kwargs """
    return a - b + c - d

def main():

    #
    # Accepting kwarg defaults
    #
    print(abcd(5, 2))

    #
    # treating kwargs as args
    #
    print(abcd(5, 2, 10, 11))

    #
    # treating kwargs as kwargs
    #
    print(abcd(5, 2, c=11, d=11))
    

if __name__ == '__main__':
    main()
