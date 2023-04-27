#!/usr/bin/env python
from __future__ import print_function
import math

def g():
    print("Sup, it's G!")
    print("Thanks, for calling!")

def f(func):
    print("Hello, I'm F.")
    print("I'm going to call 'func' now.")
    func()
    print()
    print("func's real name is {}".format(func.__name__))


def do_math(func):
    print("The function {} was passed to do_math".format(func.__name__))
    result = 0
    for x in [1, 2, 2.5]:
        print(result)
        result += func(x)
    return result


def main():
    """ This is an example of using functions as parameters.

        This is a fundamental concept of decorators.
        (See py2_functions_references.py, py2_nested_functions.py and py2_functions_returning_functions.py))
    """

    #
    # CALLING A FUNCTION AS A PARAMETER
    #
    f(g)

    print(do_math(math.sin))
    print(do_math(math.cos))


if __name__ == '__main__':
    main()
