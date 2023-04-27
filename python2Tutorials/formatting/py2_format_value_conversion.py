#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function


class Data:
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

def main():

    # Old
    print('%s %r' % (Data(), Data()))

    # New  (See the advantage here?)
    print("{0!s} {0!r}".format(Data()))




if __name__ == '__main__':
    main()