#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function
from datetime import datetime


class Plant:
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]


def main():
    """
        This is an example of Python formatting w/ named placeholders, getitem(), getattr() and datetime
        placeholders.

    """

    data = {'first': 'Edward', 'last': 'Mangini'}

    # Keyword Examples (KV Placeholders)
    print('%(first)s %(last)s' % data)      # Old
    print('{first} {last}'.format(**data))    # New
    print('{first} {last}'.format(first="Edward", last="Mangini"))  # New (This is direct kw args)

    #
    # getitem__ and __getattr__  (New method only)
    #

    person = {'first': 'Vanessa', 'last': 'Mangini'}
    fibby = [0, 1, 1, 2, 3, 5, 8, 13]

    # format supports accessing containers that support __getitem__ like dicts and lists.
    print("{p[first]} {p[last]}".format(p=person))
    print("{f[3]} {f[0]} {f[5]}".format(f=fibby))

    # it can also access attributes of objects via getattr()
    print("{p.type}".format(p=Plant()))


    # using getitem + getattr mixed together
    print("{p.type}: {p.kinds[0][name]}".format(p=Plant()))

    # datetime
    print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))


if __name__ == '__main__':
    main()
