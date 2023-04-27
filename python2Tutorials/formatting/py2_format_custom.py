#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function


class KravMaga:

    def __format__(self, format):
        if format == "bad-guy":
            return "Touch me, and your first lesson is free."
        return "KravMaga"

def main():

    print("{:bad-guy}".format(KravMaga()))


if __name__ == '__main__':
    main()
