#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Data Types and Variables
#
from __future__ import print_function
import math


def var_printer(var):
  print("\tValue: {:>20}\tType: {:<10}\t Memory: {}".format(
    var,
    str(type(var)).split('\'')[1],
    id(var)))

def main():
  """ Numbers """

  print("Integer:")
  var_printer(16)

  print("Octal")
  var_printer(oct(16))
  var_printer(020)

  print("Hex")
  var_printer(hex(16))
  var_printer(0x10)

  print("Float")
  var_printer(math.pi)

  print("Complex")
  var_printer(3+ 4j)


  # Here is a cute little while loop that keeps iterating over exponents
  # In order to increment values of 10 and 2 until we reach a 'long' type.
  print("Long: While Loop By 10s.")
  result, exponent = 0, 0
  while (isinstance(result, int)):
    result = 1 * 10 ** exponent
    exponent += 1
  var_printer(1*10**(exponent-1))
  print("\t{}".format(exponent))

  print("Long: While Loop By 2s")
  result, exponent = 0, 0
  while (isinstance(result, int)):
    result = 1 * 2 ** exponent
    exponent += 1
  var_printer(1*2**(exponent-1))
  print("\t{}".format(exponent))

if __name__ == '__main__':
    main()
