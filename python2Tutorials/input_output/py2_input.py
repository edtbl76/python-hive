#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Input and raw_input via the keyboard
#
from __future__ import print_function


def main():
    name = raw_input("What's your name? ")
    print("Nice to meet you " + name + "!")

    age = raw_input("Your age? ")
    print("So, you are already " + str(age) + " years old, " + name + "!")


if __name__ == '__main__':
    main()
