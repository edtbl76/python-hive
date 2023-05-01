#!/usr/bin/env python3

memo = {}


def fibonacci(num):

    if num < 0:
        print("Not a valid number")
        return None
    elif num <= 1:
        return num
    elif memo.get(num):
        return memo.get(num)
    else:
        memo[num] = fibonacci(num - 2) + fibonacci(num - 1)
        return memo[num]


print(fibonacci(200))
