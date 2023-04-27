#!/usr/bin/env python
from __future__ import print_function


def main():
    """ Basic example of reading in a file. """
    with open("./ad_lesbiam.txt", "r") as fobj:
        for line in fobj:
            print(line.rstrip())    # (removes the /n character at the end of every line)


if __name__ == '__main__':
    main()
