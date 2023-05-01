def binary_search(sorted_list, target):
    not_found_msg = 'value not found'
    if not sorted_list:
        return not_found_msg

    middle_index = len(sorted_list) // 2
    middle_value = sorted_list[middle_index]

    if middle_value == target:
        return middle_index

    if middle_value > target:
        left_half = sorted_list[:middle_index]
        return binary_search(left_half, target)

    if middle_value < target:
        right_half = sorted_list[middle_index + 1:]
        result = binary_search(right_half, target)

        # I hate Pythonic ternary operators...
        return result if result is not_found_msg else result + middle_index + 1


# Driver Code
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 15))
