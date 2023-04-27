#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Operators
#
from __future__ import print_function

def main():
    """ Operators """

    # In ("Element Of)
    print("If 25 is in 1-100: {}".format(True if 25 in range(1,101) else False))
    print()

    # Comparisons
    print("If 10  <  11: {}".format(10 < 11))
    print("If 10  >  11: {}".format(10 > 11))
    print("If 10  =  11: {}".format(10 == 11))
    print("If 10 !=  11: {}".format(10 != 11))
    print("If 10 <=  11: {}".format(10 <= 11))
    print("If 10 >=  11: {}".format(10 >= 11))

if __name__ == '__main__':
    main()
