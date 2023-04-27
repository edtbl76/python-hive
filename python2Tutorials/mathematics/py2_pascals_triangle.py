#!/usr/bin/env python
from __future__ import print_function


def pascal_triangle_recursion(num):
    """ Recursive Solution For Pascal's Triangle """

    if num == 1:
        return [1]
    else:
        row = [1]
        parent_row = pascal_triangle_recursion(num - 1)

        for i in range(len(parent_row) - 1):
            row.append(parent_row[i] + parent_row[i + 1])
        row += [1]
    return row


def pascal_triangle_lc(num):
    """ Pascal's Triangle using a list comprehension """

    if num == 1:
        return [1]
    else:
        parent_row = pascal_triangle_lc(num - 1)
        row = [parent_row[i] + parent_row[i + 1] for i in range(len(parent_row) - 1)]
        row.insert(0, 1)
        row.append(1)
    return row



def main():
    """ This is an example of a mathemetical solution for pascal's triangle

        Pascal's Triangle https://en.wikipedia.org/wiki/Pascal%27s_triangle
    """
    for i in range(1,10):
        int_to_str = [str(n) for n in pascal_triangle_recursion(i)]
        list_to_str = ' '.join(int_to_str)
        print("{:^30}".format(list_to_str)) # Centers the result so we get a triangle.

    print()
    for i in range(1,10):
        int_to_str = [str(n) for n in pascal_triangle_lc(i)]
        list_to_str = ' '.join(int_to_str)
        print("{:^30}".format(list_to_str)) # Centers the result so we get a triangle.


if __name__ == '__main__':
    main()
