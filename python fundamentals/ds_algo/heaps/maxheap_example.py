#!/usr/bin/env python3
from random import randrange
from max_heap import MaxHeap


max_heap = MaxHeap()

# # Example 1
# # Print attributes of empty heap
# print(max_heap.heap_list)
# print(max_heap.count)
#
# # Testing add()
# max_heap.add(42)
# print(max_heap.heap_list)


# # Example 2
# # Testing Helper Methods
# # the internal list for our example
# max_heap.heap_list = [None, 99, 22, 61, 10, 21, 13, 23]
# print(max_heap.heap_list)
# # example of how to use the helper methods:
# print("the parent index of 4 is:")
# print(max_heap.parent_index(4))
# print("the left child index of 3 is:")
# print(max_heap.left_child_index(3))
#
# # now it's your turn!
# # replace 'None' below using the correct helper methods and indexes
# idx_2_left_child_idx = max_heap.left_child_index(2)
# print("The left child index of index 2 is:")
# print(idx_2_left_child_idx)
# print("The left child element of index 2 is:")
# # uncomment the line below to see the result in your console!
# print(max_heap.heap_list[idx_2_left_child_idx])
#
# idx_3_parent_idx = max_heap.parent_index(3)
# print("The parent index of index 3 is:")
# print(idx_3_parent_idx)
# print("The parent element of index 3 is:")
# # uncomment the line below to see the result in your console!
# print(max_heap.heap_list[idx_3_parent_idx])
#
# idx_3_right_child_idx = max_heap.right_child_index(3)
# print("The right child index of index 3 is:")
# print(idx_3_right_child_idx)
# print("The right child element of index 3 is:")
# # uncomment the line below to see the result in your console!
# print(max_heap.heap_list[idx_3_right_child_idx])

# Example 3
# Completed Heapify
random_numbers = [randrange(1, 101) for n in range(6)]
for element in random_numbers:
    max_heap.add(element)
print(max_heap.heap_list)