#!/usr/bin/env python
from __future__ import print_function
import re

def main():
    """ Look at data_Structures/py2_string_split

        Regex supports a more fine grained implementation of split() than can be performed by
        string's version
    """
    raven = 'Once upon a midnight dreary, while I pondered, weak and weary, \n' \
            'Over many a quaint and curious volume of forgotten lore- \n' \
            'While I nodded, nearly napping, suddenly there came a tapping \n,' \
            'As of some one gently rapping, rapping at my chamber door. \n' \
            '"\'Tis some visitor," I muttered, "tapping at my chamber door- \n' \
            'Only this and nothing more."'

    # The Poem
    print(raven)
    print("\n\n")

    # Poem w/ string split  (NOTE: All of the special characters are still there!)
    print(raven.split())
    print("\n\n")

    # Use regex to avoid the extra characters
    print(re.split("\W+", raven))
    print("\n\n")


    """
        EX2
            This demonstrates a more powerful use of split. 
            
            We are provided w/ kv-like values from text or a document. 
            We can cycle through these if we understand the complex separator
            
            (In this case the separator is 0 or more commas, followed by 0 or more spaces, followed
            by 0 or more alphanumeric characters (this is the word before the colon) and then 
            the colon). 
    """
    pattern = r",* *\w*: "
    ceos = [
        "last: Musk, first: Elon, company: Tesla",
        "last: Zuckerberg, first: Mark, company: Facebook",
        "last: Bezos, first: Jeff, company: Amazon"
    ]
    for ceo in ceos:
        result = re.split(pattern, ceo)[1:]
        print(result)




if __name__ == '__main__':
    main()