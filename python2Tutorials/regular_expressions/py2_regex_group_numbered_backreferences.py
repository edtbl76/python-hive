#!/usr/bin/env python
from __future__ import print_function
import re


def main():
    """ This is a practical use case of regular expressions using groups to apply the concept of
        'numbered' backreferences.
    """

    """
        NOTE: Look at the second part of the search pattern. In our pattern, the text inside the
        opening XML tag is defined as the first group. Since we know this will be the first match, 
        all we have to do (as shorthand) to define the closing XML tag is provide </\1> where the
        '\1'> is refering to the backreference to the first group. 
    """
    search_pattern = r"<([ A-Za-z ]+)>(.*)</\1>"

    with open('xml.tags', 'r') as file_handle:
        print("XML Text:")
        for line in file_handle:
            print("\t{}".format(line.rstrip()))
        print()

    with open('xml.tags', 'r') as file_handle:
        print("Converted to YAML:")
        for tag in file_handle:
            result = re.search(search_pattern, tag)
            print("\t{}: \"{}\"".format(result.group(1).replace(' ', ''),result.group(2)))
    print()

    """ This example looks at using optional back references. """
    search_pattern2 = r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)"

    list_of_peeps = [
        "Mangini, Connor",
        "999-9999 Mangini, Michael",
        "999-9998 Mangini, Vanessa",
        "999-9997 Mangini, Edward",
    ]

    print("List as is:")
    for item in list_of_peeps:
        print("\t{}".format(item))
    print()

    print("Formatted List")
    for item in list_of_peeps:
        result2 = re.search(search_pattern2, item)
        print("\t{} {} {}".format(result2.group(3), result2.group(2), result2.group(1)))

if __name__ == '__main__':
    main()
