#!/usr/bin/env python
from __future__ import print_function
import traceback

def main():
    """
        This is an example of tuples.

        Benefits of tuples:
            1.) they are FASTER than lists
            2.) they are immutable, so if you are dealing w/ data that shouldn't change, use
                tuples as a preventative method against accidental change.
            3.) a TUPLE can be used as a key in a dictionary, whereas a list can't.
    """

    tup = ('tuples', 'are', 'immutable')
    print(tup)
    print(tup[0]) # Access by index

    try:
        tup[0] = "assignment"   # I said immutable!!!
    except TypeError as err:
        # This duplicates the stack trace, but by printing it harmlessly to stdout.
        print(traceback.format_exc())





if __name__ == '__main__':
    main()
