#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function

def main():

    # String old
    print('%s %s' % ('one', 'two'))

    # String new
    print("{} {}".format("one", "two"))

    # Digit old
    print('%d %d' % (1, 2))

    # Digit new
    print("{} {}".format(1, 2))

    # New W/ PlaceHolders For reordering or reuse
    print("{0} {1}".format(1, 2))
    print("{1} {0}".format(1, 2))
    print("{0} {0} {1} {1}".format(1, 2))



if __name__ == '__main__':
    main()
