#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Data Types and Variables
#
from __future__ import print_function


def var_printer(x, y):
  # Note the formatting in the first var substitution template
  print("X: {}  MemX: {}  Y: {}  MemY: {}".format(x, id(x), y, id(y)))

def main():
  """ Changing Data Types and Storage Locations """

  # Set X to an integer
  print("x = 3, y = 0")
  x, y = (3, 0)
  var_printer(x, y)

  #Set Y to X
  # NOTE: The Memory IDs are changed, so not only the values are the same...
  #       So is the MemoryID (i.e. both variables reference the same object in memory)
  print("\ny = x, Memory Id Is Same")
  y = x
  var_printer(x, y)

  # Note: if you set the variable to the same value, it won't change it, therefore it
  #       will STILL refer to both the same value and same memory location
  print("\ny = 3, Memory Id is Same.")
  y = 3
  var_printer(x, y)

  print("\ny = 2, Memory Id is different")
  y = 2
  var_printer(x, y)

  # NOTE: Python is smart. Even though X and Y have explicitly been set to the same value in separate
  #       operations, Python points them to the same location in memory to save space.
  print("\nx = 2, memory ID is same!")
  x = 2
  var_printer(x, y)


if __name__ == '__main__':
    main()
