#!/usr/bin/env python3

# Refresher on inputs
#   weight cap  = total amount of weight I can carry
#   weights     = weights of each item in an array
#   values      = values of the items in an array
#   i           = pointer to where we are in the weights and values lists.
def recursive_knapsack(weight_cap, weights, values, i):

    # base condition
    # If we aren't pointing to anything or our weight_cap is 0, then we're either done
    # or we can't do anything
    if weight_cap == 0 or i == 0:
        return 0

    # Otherwise, if the weight prior to the current pointer is greater than our capacity
    # work backwards...
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)


# Use this to test your function:
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(recursive_knapsack(weight_cap, weights, values))