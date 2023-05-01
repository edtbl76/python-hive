nums = [5, 2, 9, 1, 5, 6]


# Define swap() below:
def swap(arr, index_1, index_2):
    # stores value at arr[i1] in temp
    temp = arr[index_1]

    # replaces arr[i1] w/ arr[i2]
    arr[index_1] = arr[index_2]

    # puts the temp value in arr[i2]
    arr[index_2] = temp


swap(nums, 3, 5)
print(nums)
