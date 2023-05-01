#! /usr/bin/env python3

from max_heap import MaxHeap


def heapsort(unsorted_list):
    # empty list to store our sorted values
    sort = []

    # Set up our Max Heap
    max_heap = MaxHeap()
    for element in unsorted_list:
        max_heap.add(element)

    # Loop through the heap, pulling max value and heapifying down
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)

    return sort


# Driver Code
my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)

