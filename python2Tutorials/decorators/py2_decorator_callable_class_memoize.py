#!/usr/bin/env python
from __future__ import print_function


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    """ This is an example of Memoization w/ decorators using callable classes.

        See py2_decorator_memoization_* for more information on the technique itself.
    """
    print(fib(30))

if __name__ == '__main__':
    main()
