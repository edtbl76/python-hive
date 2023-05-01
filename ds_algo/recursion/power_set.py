def power_set(my_list):

    if len(my_list) == 0:
        return [[]]

    # slice first index
    power_set_without_first = power_set(my_list[1:])

    with_first = [[my_list[0]] + rest for rest in power_set_without_first]

    return with_first + power_set_without_first


# A power set is defined as the set or group of all subsets for any given set, including the empty set, which is
# denoted by {}, or, ϕ. A set that has 'n' elements has 2n subsets in all. For example, let Set A = {1,2,3},
# therefore, the total number of elements in the set is 3.

result = power_set([1, 2, 3, 4, 5])
print(result)

