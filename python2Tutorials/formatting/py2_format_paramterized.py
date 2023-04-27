#!/usr/bin/env python
#
#  Friends don't let friends format in python w/o https://pyformat.info
#
from __future__ import print_function
from datetime import datetime


def main():

    # ALIGNMENT AND WIDTH
    print("{:{align}{width}}".format('test', align="^", width="10"))        # New

    # PRECISION
    print('%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182))                      # Old
    print("{:.{prec}} = {:.{prec}f}".format("Gibberish", 2.7182, prec=3))   # New
    print("{:{prec}} = {:{prec}}".format("Gibberish", 2.7182, prec='.3'))     # New (Method 2)

    # WIDTH AND PRECISION
    print('%*.*f' % (5, 2, 2.7182))                                         # Old
    print("{:{width}.{prec}f}".format(2.7182, width=5, prec=2))             # New

    # DATETIME
    dt = datetime(2019, 2, 15, 10, 43)
    print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))

    # POSITIONAL ARGUMENTS
    print("{:{}{}{}.{}}".format(2.7182818284, '>', '+', 10, 3))
    print("{:{}{sign}{}.{}}".format(2.7182818284, '>', 10, 3, sign="+"))  # w/ kw argument


if __name__ == '__main__':
    main()
