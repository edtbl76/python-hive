#!/usr/env/bin python3

# Write your code below:
#
#   * = Unpacking Operator
#   - gives functions a variable number of arguments by performing
#   `positional argument packing'
#
def print_order(*order_items):
    print(order_items)


print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')
