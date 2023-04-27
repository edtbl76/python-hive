#!/usr/bin/env python
from __future__ import print_function
import traceback

def arg_test_natural_number(f):
    def helper(x):
        if isinstance(x, int) and x > 0:
            return f(x)
        else:
            raise RuntimeError("Argument is not an integer")
    return helper

def main():
    """
        This is an example of a decorator use case for checking arguments
    """

    @arg_test_natural_number
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    for i in range(1, 11):
        print(i, factorial(i))

    try:
        print(factorial(-1))
    except RuntimeError:
        print(traceback.format_exc().splitlines()[-1])



if __name__ == '__main__':
    main()
