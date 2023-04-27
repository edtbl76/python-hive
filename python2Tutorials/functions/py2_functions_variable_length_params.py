#!/usr/bin/env python
from __future__ import print_function

def main():
    """ Example of Functions that accept a variable number of parameters """

    """ Variable Length of Pos. Params"""
    def variable_number_of_positionals(*args):
        print(args)

    variable_number_of_positionals("head", "shoulders", "knees", "toes")
    print()

    """ mixing specific positional parameter(s) followed by arbitrary number of params. """
    def locations(city, *other_cities):
        print(city, other_cities)

    locations("Boston")
    locations("Boston", "Cambridge", "Somerville", "Medford", "Malden")
    print()

    """ Proving variable lengths of args in function calls. """
    def funky(one, two, three):
        print(one, two, three)

    mj = ("a", "b", "c")
    funky(*mj)

    """ Basic Example of arbitrary no. of kw params """
    def funky(**args):
        print(args)

    funky(funky="chicken", loose="goose")
    print()

    """ Using KW values in function calls """
    def direction(forward, backward, left, right):
        print(forward, backward, left, right)

    ship = {"forward": "bow", "backward": "stern", "left": "port", "right": "starboard"}
    direction(**ship)

    """ Mixing aribitrary positional and keyword parameters """
    positionals = ("attack", "retreat")
    keywords = {"left": "lead", "right": "power"}
    direction(*positionals, **keywords)

if __name__ == '__main__':
    main()
