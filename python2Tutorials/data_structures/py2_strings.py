#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Data Types and Variables
#
from __future__ import print_function


def main():
    """ Strings """

    # Basic String
    s = "Characters"
    print("String: {}".format(s))
    print()

    chars = [char for char in s]
    # String as Characters
    print("Characters of the String: {}".format(chars))

    enum = list(enumerate(chars))
    print("Enumerated with indexes: {}".format(enum))

    copy = [char for char in s[:]]
    print("Copy Of String: {}".format(copy))

    rev = [char for char in reversed(s)]
    print("Backwards with reversed built-in: {}".format(rev))

    rev2 = [char for char in s[::-1]]
    print("Backwards with slice and step: {}".format(rev2))

    # String Operations
    print()

    # Concatenation
    first = "First"
    second = "Second"
    print(first)
    print(second)
    print("Concatenated: {}".format(first + " " + second))
    print("Better (Uses .format): {} {}".format(first, second))
    print()

    # Repetition
    annoying = "Annoying"
    print(annoying)
    print(annoying*10)

    # Getting Indexes.
    msg = "Hello, World!"
    print("\n{}{}{}{}{}".format(msg[7], msg[0].lower(), msg[4], msg[-4], msg[1]))


if __name__ == '__main__':
    main()
