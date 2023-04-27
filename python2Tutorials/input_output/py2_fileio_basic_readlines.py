#!/usr/bin/env python
from __future__ import print_function


def main():
    """ Basic example of reading a file all at once.

        This stores the entire poem in memory, so we don't have to read each line from the file.
    """


    with open("./ad_lesbiam.txt", "r") as fobj:
        poem = fobj.readlines()
    print(poem)

    # Now we can iterate over the entire line.
    for line in poem:
        print(line.rstrip())


if __name__ == '__main__':
    main()
