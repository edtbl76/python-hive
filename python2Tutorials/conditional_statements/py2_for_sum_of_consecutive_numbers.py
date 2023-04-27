#!/usr/bin/env python
from __future__ import print_function

def main():

   print("Let's add consecutive numbers starting from 1.")
   num = int(raw_input("What number would you like to add to? "))

   sum = 0
   for i in range(1, num + 1):
       sum += i

   print("The sum of consecutive numbers from 1 to {} is:\n"
         "{}".format(num, sum))

if __name__ == '__main__':
    main()