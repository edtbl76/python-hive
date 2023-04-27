#!/usr/bin/env python
from __future__ import print_function
from timeit import Timer

def factorial(n):
    print("factorial has been called with n = {}".format(str(n)))
    if n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        print("Intermediate result for {} * factorial( {} ): {}".format(n, n-1, result))
        return result


def factorial_iterative(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    """ This is an example of recursion

        Recursion is a way of coding in which a function calls itself 1 or more times. Usually, it is RETURNING
        the return value of the function call

        TERMINATION CONDITION:
            a recursive function HAS to end in order to work properly in a program. This occurs such that every layer
            of recursion the solution of the problem descends towards the BASE CASE.

            BASE CASE: level of recursion where the problem can be solved w/o further recursion.


        "Recursion in Computer Science is a method where the solution to the problem is based on solving
        smaller instances of the same problem"
    """

    #
    # Factorial Example
    #
    factorial(10)
    print(factorial_iterative(10))


if __name__ == '__main__':
    main()
