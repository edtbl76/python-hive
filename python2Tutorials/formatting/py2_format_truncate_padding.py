#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function

def main():

    # Truncation
    print('|%.5s' % 'xylophone', end="|\n")             # Old
    print('|%-10.5s' % 'xylophone', end="|\n")          # Old (with pad)
    print("|{:.5}".format('xylophone'), end="|\n")      # New
    print("|{:10.5}".format('xylophone'), end="|\n")    # New (with pad)
    print("|{:+<10.5}".format('xylophone'), end="|\n")  # New (with pad and fill)


if __name__ == '__main__':
    main()
