#!/usr/bin/env python
from __future__ import print_function
import traceback


s4 = "I'm global"
s8 = 42


def main():
    """ This is an example of global vs. local variables

        (It's probably a good idea to look up functions if you haven't yet)
    """

    """ 
    This works, because the variable s has global scope, and the function is a child of that same global scope.
    """
    def f1():
        print(s1)
    s1 = "I hate spam!"
    f1()
    print()

    """
    This example demonstrates two scopes. 
        - the first print statement (inside the f2() function will access the s in its local scope, overriding
            the s in global scope [explicit vs. implicit]
        - the second print statement outside of the function accesses the s declared in global scope. 
    """
    def f2():
        s2 = "Me too."
        print(s2)
    s2 = "I hate spam!"
    f2()
    print(s2)
    print()

    """
        This demonstrates the wonder of Python. (Sarcasm).
        Since a variable has been named inside the function w/ local scope, Python assumes that the print 
        statement preceding the assignment is an error. (i.e., since explicit over implicit is used, it makes
        no assumptions about the first use of the variable w/ the same name. 
    """
    def f3():
        try:
            print(s3)
        except UnboundLocalError:
            print(traceback.format_exc().splitlines()[-1])
        s3 = "Me too."
        print(s3)

    s3 = "I hate spam."
    f3()
    print(s3)
    print()

    """
    NOTE: to make this work, s4 was defined outside of the main scope. 
    
        This addresses the conundrum in example f3(). Since Python won't assume our intent for the usage of 
        variables w/ ambiguous namespace, if a variable name is used prior to it being assigned in a specific
        namespace, then it must be decorated w/ the global keyword in order to reference the global namespace. 
        
        However, note that further internal use references the local namespace assignment AND external usage now 
        uses what was assigned locally, because the data in the var reference has been changed. 
    """
    def f4():
        global s4
        print(s4)
        s4 = "I am local"
        print(s4)

    f4()
    print(s4)
    print()

    """
        This is a demonstration of being unable to access locally created names in a global namespace.
    """
    def f5():
        s5 = 'I am local!!!'
        print(s5)

    f5()
    try:
        print(s5)
    except NameError:
        print(traceback.format_exc().splitlines()[-1])
    print()

    """
        Deliberate mix. 
        
        internal print statement
            - the first value is collecting the global s8 external from main
            - the second value is a local reference w/ the same name as a global variable 
            - the third value is a actually a local reference from a parameter, then changed locally
            - the fourth value is similar to the 3rd
            
        external print statement:
            - the first value is collecting the s8 value determined inside main. (intermediate scope!) 
            - the second value is the unchanged global variable (w/ same name as a local variable) 
            - the third value is an unchanged global variable. 
            - the fourth value is an unchanged global variable.
            
    """
    def f6(s6, s7):
        global s8   # global, external to main
        s6, s7 = s7, s6     # provided as parameters, values reset. (Behaves as call-by-reference until values change)
        s9 = 33     # global, internal to main, changed locally
        s9 = 17     # changed locally again
        s10 = 100  # Local, but never used.
        print(s8, s9, s6, s7)

    s8, s9, s6, s7 = 1, 15, 3, 4    # external to f6, local to main
    f6(17, 4)
    print(s8, s9, s6, s7)



if __name__ == '__main__':
    main()
