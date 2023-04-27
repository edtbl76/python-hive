#!/usr/bin/env python
from __future__ import print_function


def memoize(f):
    memo = {}

    def function_wrapper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return function_wrapper


def fib(n):
    """Good ole' fibonacci recursion """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    """ This is an example of 'memoization'

        This is a term introduced by Donald Michie in 1968. It is derived from the Latin 'memorandum'
        meaning 'to be remembered;.

        This is a useful performance enhancing technique in computational programs such that it allows for the
        memorization (or caching) of calculation results of processed input.

        This allows previous calculations to be stored (usually in an array) so that they don't have to be
        recalculated.

        This is especially useful for recursive structures, where the results of one iteration are stored for future
        iterations until the base_case is achieved.
    """
    fibv = memoize(fib)   # This should look familiar... it's the non-pythonic syntax for decorators.
    print(fibv(30))


if __name__ == '__main__':
    main()
