def binary_search(sorted_list, left_pointer, right_pointer, target):
    not_found_msg = 'value not found'

    # Base case (empty sublist)
    if left_pointer >= right_pointer:
        return not_found_msg

    # use the pointers to find middle index
    middle_index = (left_pointer + right_pointer) // 2
    middle_value = sorted_list[middle_index]

    # Found it!
    if middle_value == target:
        return middle_index

    # Handle Left SubList Path
    if middle_value > target:
        # all of the args are the same, but we swap the right pointer w/
        # middle index.
        return binary_search(sorted_list, left_pointer, middle_index, target)

    # ... Right Sub path
    if middle_value < target:
        # same concept as above
        return binary_search(sorted_list, middle_index + 1, right_pointer, target)


# Driver Code
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))