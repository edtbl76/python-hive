def sum_digits(n):
    if n < 10:
        return n

    last_digit = n % 10
    return last_digit + sum_digits(n // 10)