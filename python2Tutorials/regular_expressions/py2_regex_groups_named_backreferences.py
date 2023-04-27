#!/usr/bin/env python
from __future__ import print_function
import re


def main():
    """
        This is an example of named backreferences using groups in regular expressions.
    """

    date_string = "Fri Oct 15 02:35:01 EDT 1976"
    expression = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b"

    result = re.search(expression, date_string)

    """
        This if/else statement is just to make sure that we have a result before go looking for the
        group. If the result doesn't exist, this would throw an AttributeError. 
        
        Now you know. And Knowing is half the battle. 
    """
    print("Original String: {}".format(date_string))
    if result:
        print("Matched Group  : {}".format(result.group()))
    else:
        print("No Match!")

    """
        This output demonstrates the true value of named backreferences. 
        
        Here, we start with the matched 'group'. We can get the span of each named 
        group reference (including start/end values) such that the indices could be returned to 
        the caller for further operations. 
    """
    for group_name in ['hours', 'minutes', 'seconds']:
        print("{:<7}: {}\n\tSpan : {}\n\tStart: {}\n\tEnd  : {}".format(
            group_name.capitalize(),
            result.group(group_name),
            result.span(group_name),
            result.start(group_name),
            result.end(group_name)))


if __name__ == '__main__':
    main()
