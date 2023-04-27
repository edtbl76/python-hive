#!/usr/bin/env python
from __future__ import print_function


def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, {} returns:".format(func.__name__))
        func(x)
    return function_wrapper


def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, {} returns:".format(func.__name__))
        func(x)
    return function_wrapper


def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print("{}, {} returns:".format(expr, func.__name__))
            func(x)
        return function_wrapper
    return greeting_decorator

def main():
    """ This is an example of a decorators w/ parameters """

    """
        These examples show two VERY SIMILAR decorators.
    """
    @evening_greeting
    def edward(x):
        print("call")
    edward("Edward")
    print()

    @morning_greeting
    def edward(x):
        print("call")
    edward("Edward")
    print()

    """
        This simplifies the code a bit by nesting a decorator inside a function designed to handle the parameter
    """
    @greeting("Greetings Program")
    def edward(x):
        print("call")
    edward("Edward")


if __name__ == '__main__':
    main()
