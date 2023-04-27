#!/usr/bin/env
from __future__ import print_function
import re


def main():
    """ This is an example of using a regular expression where the pattern is a group of
        explicitly stated alternatives inside the

    """
    string_to_evaluate = "His head fell off!"
    pattern = r".*(head|shoulders|knees|toes).*"
    match_object = re.search(pattern, string_to_evaluate)

    # We have to check that there was a hit!
    if match_object:
        print(match_object.group())
    else:
        print("No match!")

if __name__ == '__main__':
    main()
