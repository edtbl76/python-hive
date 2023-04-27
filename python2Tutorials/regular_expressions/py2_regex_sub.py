#!/usr/bin/env python
from __future__ import print_function
import re


def main():
    """
    This is an example of find/replace using re.sub()

        The arguments are regex, the replacement to make if the regex is matched, and then the
        subject/string to be evaluated.
    """

    pattern = r"[dD]ead"
    stringy = "Dead I tell you! I'm going to be dead!"
    print(stringy)
    print()

    result = re.sub(pattern, "smelly", stringy)
    print(result)

if __name__ == '__main__':
    main()