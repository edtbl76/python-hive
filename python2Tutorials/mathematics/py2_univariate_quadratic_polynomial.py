#!/usr/bin/env python
from __future__ import print_function

def polynomial_factory(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial



def main():
    """ This is an implementation of a polynomial 'factory' function using the concept of nested functions
        that return a function
    """

    # Set the coefficients for the polynomials for the outer/top-level function
    p1 = polynomial_factory(2, 3, -1)
    p2 = polynomial_factory(-1, 2, 1)

    # set x values for the inner function
    for x in range(-2, 2, 1):
        print(x, p1(x), p2(x))

if __name__ == '__main__':
    main()
