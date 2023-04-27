#!/usr/bin/env python
from __future__ import print_function

import random


def main():
    """ This is an example of a while loop

        This is a while else loop. For the most part this operates the same
        way that a standard while loop does.

        The real value here is in the BREAK statement.

        We establish in the print statement that 0 is going to exit the loop.

        The outer if logic determines if the user wants to continue playing. If not, the break statement
        gets us out of the loop so that the while-else statement isn't executed.

        The inner if logic (if you select to continue) evaluates the input against the control.

        We have THREE things happening here.
        - The while loop evaluates whether or not the guess is correct.
        - the external if loop inside the while loop determines if the player wants to continue playing
        - assuming they do, the inner if loop evaluates "direction" of the guess to give feedback to the
          player for the next round.
    """
    n = 20
    to_be_guessed = int(n * random.random()) + 1
    guess = 0

    print("Let's play guess the number! Press 0 to exit")
    while guess != to_be_guessed:
        guess = int(raw_input("New Number: "))

        if guess != 0:
            if guess > to_be_guessed:
                print("Too Large!")
            elif guess < to_be_guessed:
                print("Too Small!")
        else:
            print("Thanks for playing! Come again! (Phrasing)")
            break
    else:
        print("You got it!")



if __name__ == '__main__':
    main()
