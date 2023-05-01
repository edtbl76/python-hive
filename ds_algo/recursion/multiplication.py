# iteration
def multiplication_iter(n1, n2):
    result = 0
    for count in range(0, n2):
        result += n1
    return result


# recursion
def multiplication(n1, n2):
    if n2 == 0:
        return 0

    return n1 + multiplication(n1, n2 - 1)
