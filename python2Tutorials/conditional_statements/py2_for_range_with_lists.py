#!/usr/bin/env python
from __future__ import print_function

def main():
    """ This is an example of iterating over for loops w/ the range() function
        using lists.
    """

    fibby = [0, 1, 1, 2, 3, 5, 8, 13, 21 ]
    for f in range(len(fibby)):
        print("{}.) {}".format(f + 1, fibby[f]))

if __name__ == '__main__':
    main()