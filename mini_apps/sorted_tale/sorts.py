import random


def bubble_sort(arr, comparison_function):
    swaps = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(len(arr) - 1):
            # if arr[idx] > arr[idx + 1]:
            if comparison_function(arr[idx], arr[idx + 1]):
                is_sorted = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print("Bubble sort: There were {0} swaps".format(swaps))
    return arr


def quicksort(my_list, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = my_list[pivot_idx]
    my_list[end], my_list[pivot_idx] = my_list[pivot_idx], my_list[end]
    less_than_pointer = start
    for i in range(start, end):
        # if pivot_element > my_list[i]:
        if comparison_function(pivot_element, my_list[i]):
            my_list[i], my_list[less_than_pointer] = my_list[less_than_pointer], my_list[i]
            less_than_pointer += 1
    my_list[end], my_list[less_than_pointer] = my_list[less_than_pointer], my_list[end]
    quicksort(my_list, start, less_than_pointer - 1, comparison_function)
    quicksort(my_list, less_than_pointer + 1, end, comparison_function)
