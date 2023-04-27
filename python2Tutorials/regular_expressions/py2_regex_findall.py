#/usr/bin/env python
from __future__ import print_function
import re


def main():
    """
        This is an example of the findall() method of the re module. (NOTE: this is Python specific, so enjoy it!)

    """

    """ The parameters for findall are the same as they are for search/match 
            
            pattern_to_match, string_to_search
            
        The result is a list of matches.
    
    """
    string = "I had the gall to fall on a ball in a hall at the mall. Don't call"
    match_object = re.findall('[bfghm]all', string)
    print(match_object)
    print()

    """ Matching This string is kludgy, not the best way to solve the problem. """
    new_string = "SSN: 999-99-999, DOB: October 29, 1981"
    pattern = r"[0-9]+.*: .*"
    match_object = re.findall(pattern, new_string)
    print(match_object)
    print()

    """ Solving the previous example by using groups 
        
        The result is a list of groups (or a list of tuples if the pattern has more than one group)
    """
    group_pattern = r"([0-9-]+).*: (.*)"
    match_object = re.findall(group_pattern, new_string)
    print(match_object)


if __name__ == '__main__':
    main()
