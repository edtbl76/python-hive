#!/usr/bin/env python
from __future__ import print_function


def add(x, y):
    """ has 2 parameters, and returns a value """
    return x + y

def add_optional(x, y=5):
    """ has 2 parameters, one of which has a default value """
    return x + y


def main():
    """ This is an introduction to Python functions
        NOTE: Recursive Functions are in the mathematics directory.
    """
    #
    # Calling Function w/ Parameters that Returns a Value
    #
    print(add(10, 10))

    #
    # Calling Function w/ optional parameter (or parameter w/ default value...)
    #
    print(add_optional(10, 10))
    print(add_optional(10))

    #
    # Docstring
    #
    print(add.__doc__)
    print(add_optional.__doc__)


if __name__ == '__main__':
    main()