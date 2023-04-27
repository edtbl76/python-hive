#!/usr/bin/env python
from __future__ import  print_function
import traceback

def main():
    """ This is an example to functions as references

        NOTE: This concept is important to understanding decorators
        (See: py2_functions_as_parameters.py, py2_functions_returning_functions.py and py2_nester_functions.py)

        Remember... a function name is a reference to the function itself...
        This means that we can assign another name to the same function
    """

    #
    # CREATE A FUNCTION (requires local scope, so its embedded)
    #
    def succ(num):
        return num + 1

    #
    # CREATE A NEW REFERENCE
    #
    """ 
        Here we are creating a new reference to the function, and using it the same
        way we would have used the original name. 
    """
    successor = succ
    print(successor(10))
    print(succ(10))

    #
    # DELETE A REFERENCE
    #   (Here we are only deleting a REF to the function. The function itself still
    #   exists)
    #
    del succ
    print(successor(10))
    try:
        print(succ(10))
    except UnboundLocalError:
        """ This demonstrates that the reference named 'succ' is gone"""
        print(traceback.format_exc().splitlines()[-1])


if __name__ == '__main__':
    main()
