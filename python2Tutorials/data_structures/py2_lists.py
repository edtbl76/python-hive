#!/usr/bin/env python
from __future__ import print_function
import traceback
import sys

def main():

    #
    # Shallow List  (A Shallow List is a single dimension list, or a primitive linear data structure)
    #
    lang = ['Python', 'Go', 'Java', 'Kotlin', 'JavaScript']
    old_langs = ['C', 'C++']
    new_langs = ('Julia', 'Rust')

    print(lang)                         # Just the list
    print(", ".join(lang))              # Format the list using Join
    print(lang[0])                      # Get item using index
    print(lang[-2])                     # Get item using negative index

    #
    # Enumerate  (the second arg to enumerate is an offset to the index)
    #
    for count, value in enumerate(lang, 1):
        print("{}.) {}".format(count, value))

    #
    # APPEND
    #
    lang.append('TypeScript')
    lang.append('Scala')
    print(lang)
    lang.append(old_langs)
    print(lang)

    """ Notice the result!. We've appended a list into a list creating a multidimensional list """

    #
    # POP (Removes AND Returns the result)
    #
    print(lang.pop())       # By default pop 'pops' the last element
    print(lang.pop(-2))     # pop supports an argument to specify an element to 'pop'

    #
    # EXTEND
    #
    lang.extend(old_langs)
    print(lang)

    """ Much better! The difference between extend and append is that append adds a sequence to a sequence, whereas
        extend adds the elements OF a sequence to a sequence. Let's prove that... """

    lang.extend('TypeScript')
    print(lang)

    """ See... by extending a string, extend looks at the chars inside. Let's clean up..."""
    for _ in range(0, len('TypeScript')):
        lang.pop()
    print(lang)

    """ Let's extend using a tuple """
    lang.extend(new_langs)
    print(lang)

    #
    # Append/Extend w/ + operator
    #
    dead_langs = ['PHP', 'Perl']
    win_langs = ["C#", '.NET']
    print(dead_langs + win_langs)

    """ Now, using the augmented operator (NOTE: Never do LIST = LIST + NEW_LIST """
    lang += (dead_langs + win_langs)
    print(lang)

    #
    # REMOVE
    #
    """ Pop destroys elements by referring to the index (or where the data lives). The downside is that you have to 
        know where that index is. Sure, there are ways of doing that, but remove() allows us to dump the data by
        the value itself. 
    """
    for i in (dead_langs + win_langs):
        lang.remove(i)
    print(lang)


    #
    # INDEX
    #
    print(lang.index('Java'))
    print(lang.index('Java', 2))    # The 2nd arg is the location of the list to start searching (inclusive)
    try:
        print(lang.index('Java', 2, 2))  # The 3rd arg is the location of the list to stop searching (exclusive)
    except ValueError as err:
        print(traceback.format_exc().splitlines()[-1])  # <-- Cool way to just get the last line.

    """ Yes, that last line is intentionally stupid. Since the 3rd argument is exclusive, if the 2nd and 3rd arg
        are the same index, there will never be a successful match. 
    """

    #
    # INSERT
    #
    lang.insert(2, 'Clojure')
    print(lang)
    lang.insert(len(lang), 'Lisp')  # <-- Insert is masquerading as append!
    print(lang)


if __name__ == '__main__':
    main()
