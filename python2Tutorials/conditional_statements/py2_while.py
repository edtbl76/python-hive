#!/usr/bin/env python
from __future__ import print_function

import random


def main():
    """ This is an example of a while loop

        This is a basic example where only the conditions inside the
        while loop determine whether or not it continues to iterate.

        (This is interactive on purpose, so that we don't get in to an
        infinite loop in the example).

        NOTE: This is somewhat kludgy. The guess happens inside the loop, so if we guess the number
        correctly the first time, we still have to iterate through the loop.
    """
    n = 20
    to_be_guessed = int(n * random.random()) + 1
    guess = 0

    while guess != to_be_guessed:
        guess = int(raw_input("New Number: "))

        if guess > to_be_guessed:
            print("Too Large!")
        elif guess < to_be_guessed:
            print("Too Small!")
        elif guess == to_be_guessed:
            print("You got it!")



if __name__ == '__main__':
    main()
