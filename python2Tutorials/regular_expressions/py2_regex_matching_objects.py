#!/usr/bin/env python
from __future__ import print_function
import re

def main():
    """ Demonstrates match objects of the re module """

    string = "Id: 151515, Date: February, 28th, 2019"
    single_pattern = r"[0-9]+"
    multi_pattern = r"([0-9]+).*: (.*)"
    """
        This is a match object w/ a single hit.
    """
    match_object = re.search(single_pattern, string)

    # Show the matching text. (if it exists)
    print("Group: {}".format(match_object.group()))
    print()

    # Show the indexes in the string that span the matched group
    print("Span: {}".format(match_object.span()))

    # This does the same thing, but we iterate over the tuple to get each value.
    for i in range(0, len(match_object.span())):
        print("\t{}".format(match_object.span()[i]))
    print()

    # Get the start/end of the span() using keywords. This is a more practical way of getting the span
    # values
    print("Start:\t{}".format(match_object.start()))
    print("End  :\t{}".format(match_object.end()))
    print()

    """
        This is a match object w/ multiple hits.
    """
    multi_match_object = re.search(multi_pattern, string)

    # Show the matching text
    print("Group: {}".format(multi_match_object.group()))
    print()

    # This is useful, but only if you know how many subgroups get created
    print(multi_match_object.group(1))
    print(multi_match_object.group(2))
    """ Note there are ways of doing this w/ a while loop and a condition that checks for
        an exception, however this is a bad code pattern. If you are going to do that, use it as an 
        absolute last resort and document your code that this is an anti-pattern and you had no other choice. 
        
        Exceptions should not be used for control flow. 
    """

if __name__ == '__main__':
    main()
