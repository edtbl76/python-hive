def palindrome_iter(my_string):

    # Odd Strings will count down by odds
    # Even strings will count down by evens.
    # final num will be 1 or 0
    while len(my_string) > 1:
        # equality test for head and tail of the string: terminates condition
        if my_string[0] != my_string[-1]:
            return False
        # Python trick for slicing the head and tail off of the structure per iteration.
        my_string = my_string[1:-1]
    return True


# recursion
def is_palindrome(my_string):
    if not my_string:
        return True

    if my_string[0] == my_string[-1]:
        return is_palindrome(my_string[1:-1])

    return False