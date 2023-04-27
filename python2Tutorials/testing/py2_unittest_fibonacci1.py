#!/usr/bin/env python
from __future__ import print_function
from ..mathematics.py2_fibonacci_module import fib
import unittest

class FibonacciTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

if __name__ == '__main__':
    unittest.main()

