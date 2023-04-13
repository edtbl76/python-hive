# define your linear_search() below...
def linear_search1(search_list, target_value):
    for i in range(0, len(search_list)):
        print(search_list[i])
        if target_value == search_list[i]:
            return i
    raise ValueError(f'{target_value} not in list')


# uncomment the lines below to test...
values = [54, 22, 46, 99]
print(linear_search1(values, 22))

number_list = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33


# Example 2
def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))


try:
    # Call the function below...
    result = linear_search(number_list, 100)
    print(result)
except ValueError as error_message:
    print("{0}".format(error_message))

# Find Multiple Instances
# Search list and target value
tour_locations = ["New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"


# Linear Search Algorithm
def linear_search_find_dupes(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)

    if matches:
        return matches
    else:
        raise ValueError("{0} not in list".format(target_value))


# Function call
tour_stops = linear_search_find_dupes(tour_locations, target_city)
print(tour_stops)

# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]


# Linear Search Algorithm
def linear_search_find_max_index(search_list):
    maximum_score_index = None
    for idx in range(len(search_list)):
        print(search_list[idx])
        if maximum_score_index is None or search_list[idx] > search_list[maximum_score_index]:
            maximum_score_index = idx
    return maximum_score_index


# Function call
highest_score = linear_search_find_max_index(test_scores)

# Prints out the highest score in the list
print(highest_score)
