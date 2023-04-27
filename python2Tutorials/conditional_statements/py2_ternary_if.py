#!/usr/bin/env python
from __future__ import print_function


def standard_if(a, b):
    """ standard if syntax """

    if a > b:
        result = a
    else:
        result = b

    return result


def ternary_if(a, b):
    """ ternary if syntax """

    result = a if (a > b) else b
    return result


def main():
    for n in range(1, 11):
        for o in range(11, 1, -1):
            # (Use the :> to right justify the var. the 2 is '2' spaces)
            # (But seriously folks, friends don't let friends format Python strings
            #  without going to pyformat.info)
            print("a={:>2}, b={:>2}, If={:>2}, TernaryIf={:>2}".format(
                n, o,
                standard_if(n, o),
                ternary_if(n, o)
            ))


if __name__ == '__main__':
    main()
