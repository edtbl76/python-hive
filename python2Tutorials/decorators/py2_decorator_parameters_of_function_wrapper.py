#!/usr/bin/env python
from __future__ import print_function
from random import random, randint, choice

def my_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling {}".format(func.__name__))
        result = func(*args, **kwargs)
        print(result)
        print("After calling {}".format(func.__name__))
    return function_wrapper

def main():
    """ Example of generalizing the parameters of the function wrapper of a decorator

        (i.e. the nested function )


    """

    rv = my_decorator(random)
    riv = my_decorator(randint)
    cv = my_decorator(choice)

    rv()
    print()

    riv(3,8)
    print()
    
    cv([4, 5, 6])


if __name__ == '__main__':
    main()
