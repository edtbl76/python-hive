#!/bin/python3
# One-file demo for shell injection.
import os, sys

global difficulty


# Not the prettiest code, but it's sufficient for this demonstration.
def startup():
    global difficulty
    print("Welcome to Shell Injection simulator!")
    difficulty = 0
    if len(sys.argv) > 1:
        param1 = str(sys.argv[1])
        if param1.lower() == "hard":
            difficulty = 1
            print("Difficulty has been set to HARD.")
        if param1.lower() == "veryhard":
            difficulty = 2
            print("Difficulty has been set to VERY HARD.")
        if param1.lower() == "impossible":
            difficulty = 3
            print("Difficulty has been set to IMPOSSIBLE. Good luck.")

    main()


# Sometimes, it's better to be readable than to be elegant.
def main():
    keepgoing = True
    while keepgoing:
        keepgoing = False
        userinput = input("Input an IPv4 address to check: ")

        if difficulty == 1 and is_invalid_hard(userinput):
            print("Invalid input Detected!")
            keepgoing = True
            continue

        if difficulty == 2 and is_invalid_very_hard(userinput):
            print("Invalid Input Detected!")
            keepgoing = True
            continue

        if difficulty == 3 and is_invalid_impossible(userinput):
            print("Invalid Input Detected!")
            keepgoing = True
            continue

        exec_ping(userinput)
    print("Goodbye!")


# The simplest form of input validation.
# It would be odd for someone to go to the effort of validating input, only to do it this badly, if not for demonstration purposes.
# All this test does is check if there's a semicolon anywhere in the input.
def is_invalid_hard(test_input):
    if ";" in str(test_input):
        return True
    return False


# Here's what an actual, poorly-done attempt at input validation might look like.
# It addresses multiple methods that could be used to inject a command.
# However, there are still methods that this will not catch. This is the danger of using default-allow validation.
def is_invalid_very_hard(test_input):
    banned_substrs = [';', '|', '&']
    for substr in banned_substrs:
        if substr in str(test_input):
            return True
    return False


# This method used default-deny rather than default-allow.
# It allows ONLY the characters REQUIRED, and no other characters.
# It is much more robust than the other examples, and is (probably) impossible to bypass.
# If you do manage to bypass it, we would love to know how you did it!
def is_invalid_impossible(test_input):
    valid_chars = "0123456789."
    for char in test_input:
        if not char in valid_chars:
            return True
    return False


# This method of running another program violates best practices for Python, and security in general.
# The "correct" way to accomplish this in python would be using the `subprocess` module.
def exec_ping(param):
    retval = os.system("ping -c 1 " + param)
    if retval == 0:
        print("Address is reachable.")
        return
    print("Address is NOT reachable.")
    return