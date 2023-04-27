#!/usr/bin/env python
from __future__ import print_function


def main():
    """ See Regex for other ways to break up strings...

        But this is a more direct method if you just want to break it up and play w/ all
        of the individual elements.
    """

    """
    EX 1
        By default, split()'s delimiter is a space. 
        The result is a list of the elements. 
    """
    string_to_split = "Hello, I'm going to get broken up into little pieces."
    print(string_to_split.split())
    print()

    """
    EX2
        The first argument to split() is a new delimiter...
        This is a way to replace colons in a Mac address w/ dashes for EUI-64 format. 
        (NOTE: it's easier just to do a str.replace()...) 
    """
    mac = "01:23:45:67:89:AB"
    print("Colons: {}\nEUI-64: {}".format(
        mac,
        '-'.join(mac.split(':')))
    )
    print()

    """
    EX3:
        The second argument allows you to specify the maximum number of splits. 
        NOTE: If the max splits doesn't break up the entire string, then the resulting list
            has a final 'the_rest' type of element storing the remainder of the string.
    """
    print(string_to_split.split(' ', 2))
    print()

    """
    EX4:
        This demonstrates a problem w/ EX3. If there are successive spaces (i.e. consecutive
        instances of the separator)... we end up w/ empty elements in the list. 
    """
    new_string_to_split = "Hello,    I  was broken   up   into little pieces."
    print(new_string_to_split.split(' ', 2))
    print()

    """
    EX5:
        This is the workaround to the EX4 scenario
    """
    print(new_string_to_split.split(None, 2))
    print()


if __name__ == '__main__':
    main()