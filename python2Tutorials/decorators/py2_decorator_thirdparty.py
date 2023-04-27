#!/usr/bin/env python
from __future__ import print_function
from math import sin, cos


def my_decorator(func):
    def function_wrapper(x):
        print("Before calling {}".format(func.__name__))
        result = func(x)
        print(result)
        print("After calling {}".format(func.__name__))
    return function_wrapper


def main():
    """ Example of decorators w/ 3rd party libs

            NOTE: the python "@<decorator>" syntax isn't supported here

    """

    sinv = my_decorator(sin)
    cosv = my_decorator(cos)

    for f in [sinv, cosv]:
        f(3.1415)


if __name__ == '__main__':
    main()

