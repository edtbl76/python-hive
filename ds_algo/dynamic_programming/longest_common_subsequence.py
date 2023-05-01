#!/usr/bin/env python3


dna_1 = "ACCGTT"
dna_2 = "CCAGCA"


def longest_common_subsequence(string_1, string_2):
    print(f'Finding the longest common subsequence of {string_1} and {string_2}')

    # Create a grid where the columns are each character
    # from one string, and the rows are each character
    # from the other string.
    #
    # We'll add an extra col and row to represent an
    # empty string or 'no character'
    grid = [[0 for column in range(len(string_1) + 1)] for row in range(len(string_2) + 1)]

    # Iterate through each cell to compare each letter
    # from one string w/ each letter from the other.
    for row in range(1, len(string_2) + 1):
        print(f'Comparing: {string_2[row - 1]}')

        for column in range(1, len(string_1) + 1):
            print(f'Against: {string_1[column - 1]}')

            if string_1[column - 1] == string_2[row - 1]:
                grid[row][column] = grid[row - 1][column - 1] + 1
            else:
                # show best value excluding either character
                # (i.e values located at prior row OR column)
                grid[row][column] = max(grid[row - 1][column], grid[row][column - 1])

    for row_line in grid:
        print(row_line)

    # build the subsequence
    result = []
    while row > 0 and column > 0:
        if string_1[column - 1] == string_2[row - 1]:
            result.append(string_1[column - 1])
            row -= 1
            column -= 1
        elif grid[row - 1][column] > grid[row][column - 1]:
            row -= 1
        else:
            column -= 1
    result.reverse()
    return "".join(result)


print(longest_common_subsequence(dna_1, dna_2))