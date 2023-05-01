def sum_to_one(n):
    result = 0
    for number in range(n, 0, -1):
        result += n
    return result