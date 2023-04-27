#!/usr/bin/env python
from __future__ import print_function
import sys
import __builtin__

def main():
    """ Complete list of C-Modules linked w/ the interpreter """
    for n, mod in enumerate(sys.builtin_module_names):
        print("{}. {}".format(n + 1, mod))

    print()
    for n, attr in enumerate(dir(__builtin__)):
        print("{}. {}".format(n + 1, attr))

if __name__ == '__main__':
    main()
