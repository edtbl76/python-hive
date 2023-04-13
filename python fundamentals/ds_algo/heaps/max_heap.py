#! /usr/bin/env python3
# noinspection PyMethodMayBeStatic
class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HELPERS.
    def parent_index(self, index):
        return index // 2

    def left_child_index(self, index):
        return index * 2

    def right_child_index(self, index):
        return index * 2 + 1

    def child_is_present(self, index):
        return self.left_child_index(index) <= self.count
    # END HELPERS

    def add(self, element):
        self.count += 1
        print(f'Adding: {element} to {self.heap_list}')

        self.heap_list.append(element)
        self.heapify_up()

    # Ensures that parent is larger than child
    # This works from the leaves towards the root
    def heapify_up(self):
        print('Heapifying Up')
        index = self.count
        while self.parent_index(index) > 0:
            child = self.heap_list[index]
            parent = self.heap_list[self.parent_index(index)]

            if parent < child:
                print(f'swapping {parent} with {child}')
                self.heap_list[index] = parent
                self.heap_list[self.parent_index(index)] = child

            index = self.parent_index(index)

        print(f'Heap Restored: {self.heap_list}')

    # Method used for HeapSort
    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None

        max_value = self.heap_list[1]
        print(f'Removing: {max_value} from {self.heap_list}')

        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print(f'Last element moved to first: {self.heap_list}')
        self.heapify_down()
        return max_value

    # Heapify Down (Used to rebalance the tree when working from the root towards the leaves)
    def heapify_down(self):
        index = 1

        # Work our way down to the leaves of the heap
        while self.child_is_present(index):
            print('Heapifying Down!')

            larger_child_index = self.get_larger_child_index(index)
            child = self.heap_list[larger_child_index]
            parent = self.heap_list[index]

            # If the parent is less, we have to swap the values to preserve the invariants of the max heap
            if parent < child:
                self.heap_list[index] = child
                self.heap_list[larger_child_index] = parent

            # Set the new index, so we can work our way down through the tree until there are no
            # more children to consider -> I.e. our loop is an empty nester :)
            index = larger_child_index

        print(f'Heap Restored!: {self.heap_list}')




    def get_larger_child_index(self, index):

        if self.right_child_index(index) > self.count:
            print('There is only a left child')
            return self.left_child_index(index)
        else:
            left_child = self.heap_list[self.left_child_index(index)]
            right_child = self.heap_list[self.right_child_index(index)]
            if left_child > right_child:
                print(f"Left Child is Larger: {left_child} > {right_child}")
                return self.left_child_index(index)
            else:
                print(f"Right Child is Larger: {left_child} < {right_child}")
                return self.right_child_index(index)
