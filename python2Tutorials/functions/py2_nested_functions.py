#!/usr/bin/env python
from __future__ import print_function

def f():
    def g():
        print("Hi, it's me, the g_function!")
        print("Thanks for callin'!")
    print("Hello, I'm the f_function.")
    print("I'm calling g() now!")
    g()


def temperature(t):
    def c2f(x):
        return 9 * x/5 + 32
    result = "It's {} degrees!".format(str(c2f(t)))
    return result

def main():
    """ This is an example of nested functions.

        This is a fundamental concept of decorators.
        (also see py2_functions_references.py, py2_functions_as_parameters.py and py2_functions_returning_functions.py)
    """

    #
    # CALL NESTED FUNCTION
    #
    f()
    print()

    print(temperature(20))
    print()



if __name__ == '__main__':
    main()
