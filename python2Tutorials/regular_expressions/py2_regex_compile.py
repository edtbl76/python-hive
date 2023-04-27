#!/usr/bin/env python
from __future__ import print_function
import re


def main():
    """
        This is an example of re.compile(pattern[,flags])

        The compile() method returns a regex object that can be used for later
        searching/replacing

        see REGEX.d for compile flags.
    """

    # First create our regex
    regex_pattern = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"

    # Compile the regex
    london_address_format = re.compile(regex_pattern)

    # Create a string and compare it like you would normally
    check_me = "7065 The Grove Ipswich IP33 2JG"
    result = london_address_format.search(check_me)
    print(result.group())


if __name__ == '__main__':
    main()