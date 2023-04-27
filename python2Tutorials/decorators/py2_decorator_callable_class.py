#!/usr/bin/env python
from __future__ import print_function


def decorator_function(f):
    def function_wrapper():
        print("Decorating {}".format(f.__name__))
        f()
    return function_wrapper


class DecoratorClass:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Decorating {}".format(self.f.__name__))
        self.f()


def main():
    """ This is an example of using a callable class as a decorator """

    """ This is just an example of a decorator function for purposes of comparison """
    @decorator_function
    def function_caller():
        print("inside function_caller()")
    function_caller()
    print()

    """ This is the example of the callable class"""
    @DecoratorClass
    def class_caller():
        print("inside class_caller()")
    class_caller()
    print()



if __name__ == '__main__':
    main()
