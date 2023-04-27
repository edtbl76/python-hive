#!/usr/bin/env python
from __future__ import print_function
from copy import deepcopy

def main():

    #
    #   PROBLEMS
    #
    x = 3
    y = x

    """ NOTE that both variables are pointing to the same location in memory, y is effectively a pointer
    """
    print(id(x), id(y))

    """ However unlike a 'real' pointer in C/C++ if we alter the value of y, things change which introduces 
        problems w/ mutable structures.
    
    """
    y = 4
    print(id(x), id(y))
    print(x, y)

    #
    # COPYING A LIST
    #
    cities =  ['Boston', 'Worcester']
    cities2 = cities
    print(cities)
    print(cities2)
    print(id(cities), id(cities2))

    cities2 = ['Lowell', 'Woburn']
    print()
    print(cities)
    print(cities2)
    print(id(cities), id(cities2))

    """ Changing the Entire structure doesn't create a problem, because we are reassigning the second reference to a 
        new piece of data.
    """

    #
    # MODIFYING ELEMENTS
    #
    cities2 = cities
    print()
    print(cities)
    print(cities2)
    print(id(cities), id(cities2))
    cities2[0] = 'Lowell'
    print(cities)
    print(cities2)
    print(id(cities), id(cities2))

    """ NOTE: changing the data in the pointer ALSO CHANGES THE DATA IN THE ORIGINAL.
        This makes sense (as we specified above... we have two NAMES or references to the same data)
        
        Since the reference is pointing to the container (i.e. the list) and not the elements inside, this is 
        viewed as modifying the data inside the container.
        
        In other words, the default behavior of Python when assigning a variable name to another variable name is
        to create a reference object/pointer.
    
    """

    #
    # SHALLOW COPY
    #
    cities = ['Boston', 'Worcester']
    cities2 = cities[:] # SHALLOW COPY!
    print()
    print(cities)
    print(cities2)
    print(id(cities), id(cities2))  # (You should notice right away that they have different memory locations)
    cities2[0] = 'Lowell'
    print(cities)
    print(cities2)

    """ Yaaay! We have different, isolated values! """

    #
    # Multiple Dimension Problems
    #
    dcl = ['Westford', 'Bedford', 'Newton South', 'Boston Latin',
           ['Concord', 'Carlisle'], ['Acton', 'Boxboro']]
    dcl2 = dcl[:]
    print()
    print(dcl)
    print(dcl2)
    dcl2[2] = 'Wayland'
    print(dcl)
    print(dcl2)

    """ No issues when modifying the top level list. """

    dcl2[4][0] = 'Lincoln'
    print(dcl)
    print(dcl2)

    """ The original issue now returns when trying to modify the sublist, because only the references were
        copied w/ the shallow copy """

    #
    # DEEPCOPY (to the rescue)
    #
    dcl2 = deepcopy(dcl)
    print()
    print(dcl)
    print(dcl2)
    dcl2[4][0] = 'Concord'
    dcl[4][1] = 'Sudbury'
    print(dcl)
    print(dcl2)


    """ Yaaaay! Now we can change the two copies autonomously of each other. """



if __name__ == '__main__':
    main()
