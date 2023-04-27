#!/usr/bin/env python
from __future__ import print_function

from math import sqrt


def main():

    print("Using For Loops and Range To Find All Pythagorean numbers")
    n = raw_input("Maximum Number? ")
    n = int(n) + 1

    for a in range(1, n):
        for b in range(a, n):
            c_square = a**2 + b**2
            c = int(sqrt(c_square))
            if ((c_square - c**2) == 0):
                print("a={:^4} b={:^4} c={:^4}".format(a, b, c))
            else:
                "No pythagorean numbers, try picking something larger next time."

if __name__ == '__main__':
    main()