#!/usr/bin/env python
from __future__ import print_function

import sys


def main():
    """ This is a way to use stdin to collect input from the keyboard one character at a time

        This is purely for academic purposes. No one would ever do this. Use raw_input (python2) instead.
    """

    print("What's your name?:")
    text = ""
    while 1:
        c = sys.stdin.read(1)
        text = text + c
        if c == '\n':
            break

    print("Input: {}".format(text))


if __name__ == '__main__':
    main()
