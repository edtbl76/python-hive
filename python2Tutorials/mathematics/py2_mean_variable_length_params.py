#!/usr/bin/env python
from __future__ import print_function
import traceback

def mean(num, *nums):
    """ This function calculates the mean w/ an arbitrary number of numbers """
    if not num:
        return
    elif not nums:
        return int(num)
    else:
        sum = num
        for n in nums:
            sum += n

    return sum / (1.0 + len(nums))


def main():
    """ Demonstration of the calculation of arithmetic mean """

    """ Passing numbers directly """
    result = mean(4, 7, 9)
    print(result)
    result = mean(4, 7, 9, 45, -3.7, 99)
    print(result)
    print()

    """ Passing Arguments as a list. """
    list_o_nums = [4, 7, 9, 45, -3.7, 99]
    try:
        print(mean(list_o_nums))
    except TypeError:
        print(traceback.format_exc().splitlines()[-1])
    print()

    """ Fixing it this time so things don't error out """
    print(mean(*list_o_nums))






if __name__ == '__main__':
    main()
