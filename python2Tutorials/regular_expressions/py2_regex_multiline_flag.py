#!/usr/bin/env python
from __future__ import print_function
import re

def main():
    """ Example of matching strings using MULTILINE flag. """
    s = "Oh, Hello there!\nHello, World!"

    print("String to Match:\n\n[{}]\n".format(s))

    # This fails, even though the second line starts w/ the correct text.
    print("Match From Beginning:\t", end=" ")
    print(re.search(r'^Hello', s))

    # Use Multiline flag to solve this
    print("Match W/ Multiline:\t", end=" ")
    print(re.search(r'^Hello', s, re.MULTILINE))

    """
        There is a limitation and we've been using the word MATCH too liberally. 
        If you notice here, this little trick only works if you are SEARCHING. 
        The re.match() method never checks anything but the BEGINNING of the string for a match.
    """
    print()
    print("Search w/ Multiline:\t", end=" ")
    print(re.search(r'^Hello', s, re.MULTILINE))
    print("Match w/ Multiline:\t", end=" ")
    print(re.match(r'^Hello', s, re.MULTILINE))

    """
        This is a shortcut. You can use re.M as an abbreviation for re.MULTILINE
    """
    print()
    print("Search w/ M:\t", end=" ")
    print(re.search(r'^Hello', s, re.M))
    print("Match w/ M:\t", end=" ")
    print(re.match(r'^Hello', s, re.M))


if __name__ == '__main__':
    main()