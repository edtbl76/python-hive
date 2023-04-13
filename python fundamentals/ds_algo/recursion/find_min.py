#iterative
def find_min_iter(my_list):
    min = None
    for element in my_list:
        if not min or (element < min):
            min = element
    return min


# recursive
def find_min(my_list, min = None):
  # if the list doesn't exist, return None.
  if not my_list:
    return min

  # if min is None or the first value is < min, return
  # set first value
  if not min or my_list[0] < min:
    min = my_list[0]

  # chop off the head, and track the minimum value.
  return find_min(my_list[1:], min)