#!/usr/bin/env python
from __future__ import print_function
import re


def main():
    """ Introduction to REGEX Character Classes
        Square brackets ([ and ]) are used to match character classes.
    """

    # Meyer, Maier, Mayer, Meier
    pattern = r"M[ae][iy]er"
    for name in ['Meyer', 'Maier', 'Mayer', 'Moyer', 'Meier', 'Myer']:
        if re.search(pattern, name):
            print("{} is a valid German spelling.".format(name))
        else:
            print("{} is not a valid German spelling.".format(name))
    print()


if __name__ == '__main__':
    main()

