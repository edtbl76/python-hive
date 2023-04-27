#!/usr/bin/env python
from __future__ import print_function

def cycle_list(mylist):

    if not mylist:
        return

    if isinstance(mylist, list):
        print(mylist)
        for i in range(0, len(mylist)):
            cycle_list(mylist[i])
    else:
        print(mylist)


def main():

    # Sublists (2-dimensional array)
    person = [['John', 'Doe'], ["13, Bubkiss Street", "Boston", "MA"], "99999"]

    name = person[0]
    print(name)

    first_name = person[0][0]
    last_name = person[0][1]
    print(first_name, last_name)

    address = person[1]
    street = person[1][0]
    print(street)

    # Complex Multidimensional array
    complex = ["a", ["b", ["c", ["d", "e"]]]]
    print()
    print(cycle_list(complex))





if __name__ == '__main__':
    main()
