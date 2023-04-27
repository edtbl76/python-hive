#!/usr/bin/env python
from __future__ import print_function
import sys

def main():
    """ This is an example of command line arguments

        You have to run this from the terminal

        ./py2_functions_cli_arguments.py <arg1> <arg2> . . . <argN>
    """

    for each in sys.argv:
        print(each)

if __name__ == '__main__':
    main()
