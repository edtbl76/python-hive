#!/usr/bin/env python
from __future__ import print_function


def arbitrary(x, y, *more):
    """ Notice that this function doesn't return a value
        It executes the print statement for us! How Nice. 
    """
    print("x={}, y={}".format(x, y))
    print("arbitrary: {}".format(more))

def main():

    #
    # Specify standard positional arguments
    #
    arbitrary("X", "Y")

    #
    # add in the arbitrary arguments
    #
    arbitrary(24, 23, "Super", "Cali", "Fragile", "Istic", "Expy", "Alli", "Docious")


if __name__ == '__main__':
    main()
