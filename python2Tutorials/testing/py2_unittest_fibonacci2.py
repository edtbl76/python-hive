#!/usr/bin/env python
from __future__ import print_function
from ..mathematics.py2_fibonacci_module import fib
import unittest

class FibonacciTest(unittest.TestCase):

    def setUp(self):
        self.fib_elements = (
            (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)
        )
        print("Test Setup Completed")

    def testCalculation(self):
        for (i, val) in self.fib_elements:
            self.assertEqual(fib(i), val)

    def tearDown(self):
        self.fib_elements = None
        print("TearDown Complete.")

if __name__ == '__main__':
    unittest.main()

