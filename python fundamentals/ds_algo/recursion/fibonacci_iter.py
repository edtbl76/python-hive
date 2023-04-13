def fibonacci(n):
    if n < 0:
        ValueError("Input 0 or greater only!")

    # Memoization, maintain a list of the fib numbers, for easy retrieval
    # - build a starter list w/ 0 and 1 to handle our "base cases"
    fib_list = [0, 1]

    # If n is already in our starter list, just return that value.
    if n <= len(fib_list) - 1:
        return fib_list[n]

    # This is deceiving...
    # We create a while loop that iterates through a list, but rather
    #  than decrementing n, we are appending values to the list, so the
    #  length of the list is increasing to meet n.
    while n > len(fib_list) - 1:
        # we append the next fibonacci value at the end of the list per
        # iteration.
        fib_list.append(fib_list[-1] + fib_list[-2])

    # Once the list reaches n size, we return the tail of the list.
    return fib_list[-1]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)