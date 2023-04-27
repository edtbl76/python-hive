#!/usr/bin/env python
#
#  https://python-courses.eu
#  Python 2
#  - Operators
#
from __future__ import print_function


def main():
    """ Operators """

    # BITWISE NOT (Negation)
    print()
    print("  Binary 7 =  {}".format(bin(7)))
    print("~ Binary 7 = {} [{}]".format(bin(~7), ~7))

    # Bitwise OR

    pairs = [(8,16), (5,7), (0,10), (255, 252), (1,4), (2,1)]
    for pair in pairs:
      # Display Numbers in Binary
      for num in pair:
          print("Binary {0:<11} = {0:08b}".format(num))

      a, b = pair
      #Bitwise Or
      print("Binary {0:^4} | {1:^4} = {2:08b} [{2}]".format(a, b, a|b))

      #Bitwise And
      print("Binary {0:^4} & {1:^4} = {2:08b} [{2}]".format(a, b, a&b))

      #Bitwise XOR
      print("Binary {0:^4} ^ {1:^4} = {2:08b} [{2}]".format(a, b, a^b))

      #Bitshift Left
      print("Binary {0:^4} << {1:^4} = {2:08b} [{2}]".format(a, b, a<<b))

      #Bitshift Right
      print("Binary {0:^4} >> {1:^4} = {2:08b} [{2}]".format(a, b, a>>b))


      print()


if __name__ == '__main__':
    main()
