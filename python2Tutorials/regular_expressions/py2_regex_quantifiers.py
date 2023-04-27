#!/usr/bin/env python
from __future__ import print_function
import re


def main():
    """ This demonstrates the use of quantifiers in regular expressions """

    p1 = r'[0-9]'
    p2 = r'[0-9]*'
    p3 = r'[0-9]+'
    p4 = r'[0-9]{2}'
    p5 = r'([0-9][0-9])'

    for s in ['5', '55']:
        print("Matching [{}]".format(s))

        # Matches a number. This will match both
        print("\twith [{}]:\t{}".format(p1, re.search(p1, s)))

        # Matches 0 or more numbers, both will match.
        print("\twith [{}]:\t{}".format(p2, re.search(p2, s)))

        # Matches 1 or more numbers, both will match
        print("\twith [{}]:\t{}".format(p3, re.search(p3, s)))

        # Matches exactly 2 numbers. Only the second value matches.
        print("\twith [{}]:\t{}".format(p4, re.search(p4, s)))

        # Matches exactly 2 numbers. (This does the same thing as the previous example
        # but by grouping two character classes together)
        print("\twith [{}]:\t{}".format(p5, re.search(p5, s)))


if __name__ == '__main__':
    main()
