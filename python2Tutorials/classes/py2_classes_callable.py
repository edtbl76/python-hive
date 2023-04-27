#!/usr/bin/env python
from __future__ import print_function

class A:

    def __init__(self):
        print("A has been instantiated into an Object")

    def __call__(self, *args, **kwargs):
        print("Arguments are: {} {}".format(args, kwargs))


def main():
    """ This is an example of using the __call__ method of a class """

    x = A()
    print("Now calling the instance: ")
    x(3, 4, x=11, y=10)
    print("Call it again!")
    x(3, 4, x=11, y=10)


if __name__ == '__main__':
    main()
