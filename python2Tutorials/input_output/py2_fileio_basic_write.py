#!/usr/bin/env python
from __future__ import print_function
import os

def main():
    """ Basic example of writing a file """

    if os.path.exists("./ad_lesbiam2.txt"):
        os.remove("./ad_lesbiam2.txt")

    with open("./ad_lesbiam.txt", "r") as fobj_read:
        i = 1
        for line in fobj_read:
            print(line.rstrip())
            with open("./ad_lesbiam2.txt", "a") as fobj_write:
                fobj_write.write("{}: {}".format(str(i), line))
            i = i + 1



if __name__ == '__main__':
    main()
