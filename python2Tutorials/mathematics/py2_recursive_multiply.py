#!/usr/bin/env python
from __future__ import print_function

def multiply_by(num, multiplier):

    if num == 1:
        return multiplier
    else:
        return multiply_by(num - 1, multiplier) + multiplier


def main():

    for m in range(1, 10):
        for n in range(1, 10):
            print("Num: {}  Multiplier: {} Result:{:>4}".format(n, m, (multiply_by(n, m))))


if __name__ == '__main__':
    main()