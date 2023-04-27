#!/usr/bin/env python
from __future__ import print_function
import re

def main():
    """ Example of matching from the beginning and end of strings

    """
    s1 = "Hello World!"
    s2 = "Oh, Hello"

    for s in [s1, s2]:
        print("String To Match: [{}]".format(s))
        print("\tAmbiguous:     ", end=" ")
        print(re.search(r"Hello", s))
        print("\tFrom Beginning:", end=" ")
        print(re.search(r"^Hello", s))
        print("\tFrom End      :", end=" ")
        print(re.search(r"Hello$", s))
        print()


if __name__ == '__main__':
    main()