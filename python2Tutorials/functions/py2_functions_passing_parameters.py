#!/usr/bin/env python
from __future__ import print_function


def main():
    """ This is an example of parameter passing

        CALL-BY-VALUE(a.k.a PASS-BY-VALUE)
            - C/C++ method of evaluating parameters
            - the arg expression is evaluated and the result of this evaluation is bound to the
            corresponding variable in the function.
            - if the expression is a variable, a local copy of its value is used.
            (The variable in the caller's scope will be unchanged when the function returns)

        CALL-BY-REFERENCE(a.k.a pass-by-reference)
            - Perl uses this by default (C/C++ supports it)
            - function gets an implicit reference to the argument rather than a copy of its value
                - NOTE: This means that the function can MODIFY the argument and the value of the
                        variable in the caller's scope can be changed.
            - The advantage is greater time and space efficiency because arguments don't need to be
            copied.
            - The disadvantage is that variables can be accidentally changed in function calls.

        CALL-BY-OBJECT (a.k.a CALL-BY-OBJECT-REFERENCE or CALL-BY-SHARING)
            - Python default
            - immutable arguments (ints, strings, tuples) behave like CALL-BY-VALUE.
                - object ref is passed to function params, but since the structures are immutable
                they are protected from being changed.
            - mutable structures (i.e. a list) behave differently
                - 2 cases:
                    - elements of a list can be changed in place (and this is changed in the caller's scope)
                    - if a new list is assigned to the name, the list is the caller's scope is unchanged.

    """

    """ Call By Object Example (Python Method of Passing Arguments) 
    
        By default, Python behaves like CALL-BY-REFERENCE, however as soon as 
        the value of the variable is changed, it switches to CALL-BY-VALUE. 
        
        NOTE: we are using an immutable int, so the caller's scope isn't changed. 
    """
    def reference_demo(x):
        print("x={} id={}".format(x, id(x)))
        x = 42
        print("x={} id={}".format(x, id(x)))

    x = 9
    print("Before: x={} id={}".format(x, id(x)))
    reference_demo(x)
    print("After: x={} id={}".format(x, id(x)))
    print()

    """ 
        EXAMPLE 2:
        Mutable object example (list) - changing the list
        
        Here we can see that by assigning a NEW LIST to the variable name inside the function, 
        the caller's scope isn't changed. 
    """
    def func1(plist):
        print(plist)
        plist = [47, 11]
        print(plist)

    fib = [0, 1, 1, 2, 3, 5, 8]
    func1(fib)
    print(fib)
    print()

    """
       EXAMPLE 3:
       Mutable object example (list) - changing the elements
       
       Here we can see that altering the elements in the list results in a change that affects the
       caller's scope as well, because the structure isn't immutable. 
       
    """
    def func2(plist):
        print(plist)
        plist += [47, 11]
        print(plist)

    fib = [0, 1, 1, 2, 3, 5, 8]
    func2(fib)
    print(fib)



if __name__ == '__main__':
    main()
