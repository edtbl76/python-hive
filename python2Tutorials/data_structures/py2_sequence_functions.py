#!/usr/bin/env python
from __future__ import print_function

def main():
    """
        This is another tutorial focused more on functions that support the data structures than the structure itself

        A sequence in python is defined as a LIST, TUPLE or STRING
    """

    family = ["Ed", "Vanessa", "Mike", "Connor"]

    # LENGTH
    print(len(family))

    # CONCATENATION
    surname = "Mangini"
    for first_name in family:
        print(first_name + " " + surname)   # Syntactical Concatenation
        print(first_name, surname)          # Concatenation by using print_function's default sep=" " argument.
        print("{} {}".format(first_name, surname ))     # using format

    extended = ["Bob", "Chris", "Ed Sr.", "Linda", "Jen", "Brian"]
    print(extended + family)    # CONCAT of 2 LISTS

    family += extended
    print(family)               # CONCAT of 2 LISTS using augmented assignment operator. (less clear, but cool)

    # MEMBERSHIP CHECKS
    print("Ed" in family)           # Basic Boolean
    print("Ty" in family)

    if "Jesse" in family:
        print("Brother In Law!")    # Performing operations based on result of membership checks.
    else:
        print("Adding Jesse")
        family.append("Jesse")
        print(family)

    if "Ty" not in family:
        print("Thank God!")

    # REPETITION
    print(family*2)                 # This is the same as family + family.
    family *= 2                     # Same thing using augmented assignment operator
    print(family)

    x = ['a', 'b', 'c']
    print()
    print(x)            # Normal List
    y = [x] * 4
    print(y)            # multidimensional list created via repetition

    y[0][0] = "m"
    print(y)

    """ 
        REMEMBER! When we created the new list it contained 4 nodes pointing to the SAME DATA. Modifying any element
        of any of those sublists is modifying that shared data. 
        
        This is why we use tuples if we don't want data to change! (Or conversely, you could have created a copy
        of the lists) 
    """



if __name__ == '__main__':
    main()
