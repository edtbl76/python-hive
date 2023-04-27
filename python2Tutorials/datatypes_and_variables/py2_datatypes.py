#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Data Types and Variables
#
from __future__ import print_function


def var_printer(var):
  # Note the formatting in the first var substitution template
  print("Data: {:>10}\tType: {:<10}\t Memory: {}".format(
    var,
    str(type(var)).split('\'')[1],
    id(var)))

def main():
  """ Changing Data Types and Storage Locations """


  # Set i to int and print data + type
  i = 42
  var_printer(i)

  # Change type to float by adding a float to it, reprint
  i += 0.11
  var_printer(i)

  # Change it to a string.
  i = "forty"
  var_printer(i)


  """ PART 2: assignment... """

  # assignh a value to x
  x = 3
  var_printer(x)


  # Assign x to a new variable y
  # NOTE: the storage location will be identical. We are simply creating a new reference to
  #       the exact same location in storage
  y = x
  var_printer(y)


  # Assign a new value to y, and it changes both the value AND the storage location.
  # NOTE: printing out the original variable shows the original value AND storage location.
  y = 2
  var_printer(y)
  var_printer(x)


if __name__ == '__main__':
    main()
