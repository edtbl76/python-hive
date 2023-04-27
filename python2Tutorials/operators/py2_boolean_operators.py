#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Operators
#
from __future__ import print_function


def main():
    """ Operators """

    # Boolean And, Or NOT
    for x in range(1, 5):
      # or
      print("If {} is 1 or 2:  {}".format(x, x if (x == 1 or x == 2) else False))

      # And
      print("If {} is 1 and 2: {}".format(x, x if (x == 1 and x == 2) else False))

      #NOT
      print("If {} is not 1:   {}".format(x, True if x !=1 else "It is {}!".format(x)))
      print()


if __name__ == '__main__':
    main()
