#!/usr/bin/env python
from __future__ import print_function
import re


def search_example(pattern):

    string = "A cat and a rat can't be friends."
    print(re.search(pattern, string))


def main():
    """ Basic usage of python 're' module """

    search_example("cat")   # Result is an SRE_Match Object (which means the pattern was found.)
    search_example("cow")   # Result is none, which means the pattern wasn't found.


if __name__ == '__main__':
    main()
