#!/usr/bin/env python
from __future__ import print_function


def main():
    """ This is an example of a for loop using python's range() function

        The range function has three args.

        begin (inclusive) - this is the number you start from
        end (exclusive) - this is the number that stops the sequence.
        step (the interval between elements of the sequence)
    """

    print("Count by ones")
    for n in range(1, 11):
        print(n, end=" ")

    print("\n\nCount by twoes")
    for n in range(1, 22, 2):
        print(n, end=" ")

    print("\n\nCountdown!")
    # Note the step is a negative number here, which allows us to count backwards
    for n in range(10, 0, -1):
        print(n)





if __name__ == '__main__':
    main()
