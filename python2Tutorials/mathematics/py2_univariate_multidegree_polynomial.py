#!/usr/bin/env python
from __future__ import print_function

def polynomial_factory(*coefficients):
    def polynomial(x):
        result = 0
        for index, coefficient in enumerate(coefficients):
            result += coefficient * x ** index
        return result
    return polynomial



def main():
    """ This is an implementation of a polynomial 'factory' function using the concept of nested functions
        that return a function
    """

    # Set the coefficients for the polynomials for the outer/top-level function
    p1 = polynomial_factory(4)
    p2 = polynomial_factory(2, 4)
    p3 = polynomial_factory(2, 3, -1, 8, 1)
    p4 = polynomial_factory(-1, 2, 1)

    # set x values for the inner function
    for x in range(-2, 2, 1):
        print(x, p1(x), p2(x), p(3), p(4))

if __name__ == '__main__':
    main()
