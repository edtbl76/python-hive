#!/usr/bin/env python
from __future__ import print_function
from functools import wraps

def greeting(func):
    def function_wrapper(x):
        """ function wrapper of greeting """
        print("Hi, {} returns:".format(func.__name__))
        return func(x)
    return function_wrapper


def greeting_with_wraps(func):
    def function_wrapper(x):
        """ function wrapper of greeting """
        print("Hi, {} returns:".format(func.__name__))
        return func(x)
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__
    return function_wrapper


def greeting_with_imported_wraps(func):
    """ A decorator within a decorator! Inception! """
    @wraps(func)
    def function_wrapper(x):
        """ function wrapper of greeting """
        print("Hi, {} returns:".format(func.__name__))
        return func(x)
    return function_wrapper


def main():
    """ Example of using functools wraps with decorators """

    """ First Example: We call the functools wraps in the main body of code
    
        Oops... we are getting information about the function wrapper instead of 
                the f() function.
    """
    @greeting
    def f(x):
        """ just some silly function """
        return x + 4

    f(10)
    print("function name: {}".format(f.__name__))
    print("docstring: {}".format(f.__doc__))
    print("module name: {}".format(f.__module__))
    print()

    """ Second Example: We call the functools wraps from the decorator itself 
        
        Yay! Correct results. 
    """
    @greeting_with_wraps
    def f(x):
        """ same silly function """
        return x + 4
    f(10)
    print("function name: {}".format(f.__name__))
    print("docstring: {}".format(f.__doc__))
    print("module name: {}".format(f.__module__))
    print()

    """
        Last as always: The Easy way. Import wraps from functools, and we get avoid all of the
        code inside the decorator
    """
    @greeting_with_imported_wraps
    def f(x):
        """ same silly function... again """
        return x + 4

    f(10)
    print("function name: {}".format(f.__name__))
    print("docstring: {}".format(f.__doc__))
    print("module name: {}".format(f.__module__))
    print()





if __name__ == '__main__':
    main()
