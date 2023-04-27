#!/usr/bin/env python
from __future__ import print_function
import math
import __builtin__

def main():
    """ Using dir() with modules """

    """ Dir w/ no argument gets a list w/ the names in the current local scope """
    print(dir())
    print()

    """ Dir w/ an argument lists the valid attributes + methods of the module """
    for n, attr in enumerate(dir(math)):
        print("{}. {}".format(n + 1, attr))


if __name__ == '__main__':
    main()
