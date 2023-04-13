# Define sum_to_one() below...
def sum_to_one(n):
    # Base Case
    if n == 1:
        return n

    # Recursive Step
    print("Recursing with input: {}".format(n))
    return n + sum_to_one(n - 1)


# uncomment when you're ready to test
print(sum_to_one(7))