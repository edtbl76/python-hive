nums = [5, 2, 9, 1, 5, 6]


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


# define bubble_sort():
def bubble_sort(arr):
    # The Outer loop
    for element in arr:
        # Second Loop in Bubble Sort iterates up to
        #   the last element (exclusive)
        #
        #   We exclude the last element to avoid an
        #   overflow
        #
        #   This loop will only move the largest value
        #   To its correct placement on its own.
        #   In order to sort the entire structure,
        #   this loop must be nested in the outer loop
        for index in range(0, len(arr) - 1):
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)


##### test statements

print("Pre-Sort: {0}".format(nums))
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))