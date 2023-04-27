#!/usr/bin/env python
from __future__ import print_function


def my_decorator(func):
    def function_wrapper(x):
        print("Before calling {}".format(func.__name__))
        func(x)
        print("After calling {}".format(func.__name__))
    return function_wrapper


def main():
    """ Example of a simple decorator """

    def my_func(x):
        print("Hi! I've been called with {}".format(str(x)))

    print("Calling my_func before decoration:")
    my_func("Hello World!")
    print()

    print("Decorate my_func with f:")
    my_func = my_decorator(my_func)
    print()

    print("Calling MyFunc after it has been decorated")
    my_func(42)
    print()

if __name__ == '__main__':
    main()

