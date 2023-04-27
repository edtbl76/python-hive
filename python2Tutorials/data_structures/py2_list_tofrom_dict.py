#!/usr/bin/env python
from __future__ import print_function


def main():

    #
    # DICTS TO LISTS
    #
    kids = {"Mangini": ["Connor", "Mike"], "Underwood": "Parker", "Perry": "James"}
    print(list(kids.items()))   # Becomes a list of tuples (w/ that one list inside!
    print(list(kids.keys()))    # List of Keys
    print(list(kids.values()))  # List of Values

    #
    # LISTS TO DICTS
    #
    print()
    cities = ["Seattle", "Los Angeles", "Glendale", "San Francisco"]
    mascots = ["Seahawks", "Rams", "Cardinals", "49ers"]

    #
    # ZIP (combines and creates an iterator) SLOW WAY
    #
    nfc_west_iterator = zip(cities, mascots)
    print(nfc_west_iterator)    # Iterator

    nfc_west_tuples = list(nfc_west_iterator)
    print(nfc_west_tuples)             # Now we have a list of tuples

    nfc_west = dict(nfc_west_tuples)
    print(nfc_west)

    #
    # FASTER VERSION
    #
    print(dict(zip(cities, mascots)))

    #
    # WHAT IF THE TWO LISTS ARE UNEVEN ?
    #
    cities.append("St.Louis")
    print(dict(zip(cities, mascots)))

    """ The output is the same.... zip() only generates tuples up to the point where the two lists both
        have elements and truncates the rest
    """







if __name__ == '__main__':
    main()
