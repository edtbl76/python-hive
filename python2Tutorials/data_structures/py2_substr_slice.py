#!/usr/bin/env python
from __future__ import  print_function


def main():
    """ This is isn't a data structure itself as much as it is a sub-structure of an existing
        structure.

        Python uses the term 'slicing', while many other languages call this substr or substring.
        Given the scope of the feature, I decided to create a separate 'tutorial' for this.

        NOTE: this works on lists and strings, but my examples are only going to be for strings.
    """

    str = "Ed Mangini"
    print(str[0:2])     # Start from index 0 and create a 2 character slice
    print(str[0:-8])    # Start from index 0, and omit the last 8 characters.
    print(str[3:])      # Start from index 3 and get the remaining characters of the original structure

    """ Creates a copy of the string (this is useful when you want to perform an operation on a list that involves 
        altering the list during the iteration """
    print(str[:])

    print(str[::2])     # Prints every second character  (i.e. this is a step argument.)
    print(str[::-1])    # Prints the string backwards. 







if __name__ == '__main__':
    main()
