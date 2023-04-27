#!/usr/bin/env python
from __future__ import print_function
import traceback


def main():
    """ This is an example of a set.

        This is derived from mathematical sets, such that in Python a set is an unordered collection
        of unique and immutable objects.
    """

    #
    # Set
    #
    msg = "Diabetes Sucks."
    print(msg)
    print(set(msg))

    print()
    cities = ["Foxboro", "East Rutherford", "Miami", "Buffalo", "East Rutherford", "Dallas", "Washington, D.C.",
              "East Rutherford"]
    print(cities)
    print(set(cities))

    #
    # SETS DON'T SUPPORT MUTABLE DATA TYPES
    #
    print()
    tup = (("I'm", "immutable"), ["I'm", "Not"])
    print(tup)
    try:
        print(set(tup))
    except TypeError:
        print(traceback.format_exc().splitlines()[-1])

    #
    # SETS ARE MUTABLE
    #
    print()

    """ You can use curly braces as a shortcut to declaring a set. """
    titans = {'Nightwing', 'Beast Boy', 'Starfire', 'Raven'}
    print(titans)

    # ADD
    titans.add('Superboy')
    print(titans)

    # COPY (SHALLOW)
    shallow = titans.copy()
    print(shallow)    # Note that a copy returns an UNORDERED collection.

    # DIFF
    orig_titans = {'Robin', 'Cyborg', 'Starfire', 'Kid Flash', 'Speedy', 'Raven', 'Changeling', 'Wonder Girl'}
    print(titans.difference(orig_titans))
    print(titans - orig_titans)     # This is a shortcut notation for diff
    print(orig_titans - titans)

    titans.difference_update(orig_titans)   # this could be written titans = titans - orig_titans
    print(titans)
    print(orig_titans)

    # DISCARD + REMOVE  A SINGLE ELEMENT
    titans.discard("Superboy")
    print(titans)

    """ The difference between discard and remove is that discard does nothing if the key doesn't 
        exist, while remove returns a KeyError. 
    """
    titans.discard("Superboy")
    try:
        titans.remove("Superboy")
    except KeyError:
        print(traceback.format_exc().splitlines()[-1])

    # ISDISJOINT (returns true if two sets have NULL intersection)
    print(titans.isdisjoint(orig_titans))

    # IS SUBSET (returns true if set is subset of another)
    orig_titans.add('Nightwing')
    orig_titans.add('Beast Boy')
    print(titans.issubset(orig_titans))

    # IS SUPERSET (returns true if set is superset of another)
    print(orig_titans.issuperset(titans))

    # INTERSECTION (returns the intersection of two sets)
    print(titans.intersection(orig_titans))
    print(titans & orig_titans) # Abbreviated

    # POP (removes arbitrary element)
    for _ in range(1, len(orig_titans)):
        print(orig_titans.pop())

    # CLEAR
    titans.clear()
    print(titans)

    #
    # Frozen Sets  (While sets don't support immutable elements, they themselves ARE MUTABLE)
    #               (Frozen Sets are IMMUTABLE)
    #
    print()
    frozen = frozenset(['Olaf', 'Anna'])
    print(frozen)
    try:
        frozen.add('Elsa')
    except AttributeError:
        print(traceback.format_exc().splitlines()[-1])



if __name__ == '__main__':
    main()
