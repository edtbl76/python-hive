#!/usr/bin/env python
from __future__ import print_function
import pickle
import sys


def main():
    """ Example of Pickle.

        Pickle is a module that includes algorithms for serialization/de-serialization of python object structures

        This process converts a Python object hierarchy into a byte stream (and then unpickles it at the other end).
        This serialization/flattening of a data structure is typically done for the purposes of storing the state
        of an object hierarchy in order to use it later.


    """

    # Pickle me!
    data = (1.4, 42)
    with open('data.pkl', 'w') as output:
        pickle.dump(data, output)   # Serializing it here.

    # (Open the file to look at how ugly it looks) - it's bytes

    # Unpickle me!
    with open('data.pkl') as input:
        new_data = pickle.load(input)
    print(new_data)


if __name__ == '__main__':
    main()
