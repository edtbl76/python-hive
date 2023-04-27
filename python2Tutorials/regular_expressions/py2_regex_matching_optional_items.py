#!/usr/bin/env python
from __future__ import  print_function
import re


def main():
    """ This is a demonstration of matching optional characters """

    """
        This is the same example we used in character classes. 
        However, the e is now made optional by being followed w/ a '?' symbol. 
    """
    pattern = r"M[ae][iy]e?r"
    for name in ['Meyer', 'Maier', 'Mayer', 'Moyer', 'Meier', 'Myer', 'Mayr', 'Meyr', 'Meir', 'Mair']:
        if re.search(pattern, name):
            print("{} is a valid German spelling.".format(name))
        else:
            print("{} is not a valid German spelling.".format(name))
    print()


    pattern2 = r"Mar(ch)?"
    print(re.search(pattern2, "March 2011"))
    print(re.search(pattern2, "Mar 2011"))

if __name__ == '__main__':
    main()
