#!/usr/bin/env python
from __future__ import  print_function


def f(x):
    def g(y):
        return y + x + 3
    return g

def main():
    """ example of functions returning functions.

        This is a requisite concept for understanding decorators
        (See py2_functions_as_parameters, py2_functions_references, and py2_nested_functions)
    """

    """ Remember, we are creating references to the function itself, so the variable is a name that points to a 
        memory location (the same memory location by default). 
        
        The parameter being passed here is being passed to the top level function
        
    """
    nf1 = f(1)
    nf2 = f(3)

    """ By calling the reference to the function, we gain access to the internal function (g)
    """
    print(nf1(1))
    print(nf2(1))

if __name__ == '__main__':
    main()
