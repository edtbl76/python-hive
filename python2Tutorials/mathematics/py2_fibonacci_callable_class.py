#!/usr/bin/env python
from __future__ import print_function


class Fibonacci:

    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n - 1) + self.__call__(n - 2)
        return self.cache[n]


def main():
    """ This is an example of a callable class to calculate Fibonacci """

    fib = Fibonacci()
    for i in range(15):
        print(fib(i), end=", ")


if __name__ == '__main__':
    main()
