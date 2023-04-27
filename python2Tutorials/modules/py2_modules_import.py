#!/usr/bin/env python
from __future__ import print_function


def import_module_example():
    """ demonstrates importing the entire module"""
    import fibonacci
    print(fibonacci.fib(5))
    print(fibonacci.ifib(6))


def rename_module_functions():
    """ allows us to create a reference to imported functions
        for abbreviated readability (or potentially to avoid collisions)
    """

    import fibonacci
    fibby = fibonacci.fib
    ifibby = fibonacci.ifib
    print(fibby(7))
    print(ifibby(8))


def import_names_directly():
    """ allows us to import only what we need, saving resources, and keeping code clean.
    """
    from fibonacci import fib, ifib
    print(fib(9))
    print(ifib(10))


def renaming_module_namespace():
    """ allows us to rename modules to support multiple versions, prevent collisions,
        shorten names etc.
    """
    import fibonacci as f
    print(f.fib(11))
    print(f.ifib(12))

def main():
    """ Various Examples of Module Imports"""
    import_module_example()
    rename_module_functions()
    import_names_directly()
    renaming_module_namespace()

if __name__ == '__main__':
    main()
