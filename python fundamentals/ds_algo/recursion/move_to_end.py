def move_to_end(lst, val):
    # create an empty list
    result = []

    # Base Case checks for empty list
    if len(lst) == 0:
        return []

    # RECURSIVE STEP
    # - if the first element matches our value...
    if lst[0] == val:
        # slice the value from the list, and send the sliced list back through
        # the recursive function
        result += move_to_end(lst[1:], val)

        # once the recursive call returns, slap the value at the end of the list
        result.append(lst[0])
    else:
        # If the element isn't our value, then append it to the end of the list...
        result.append(lst[0])

        # ... by doing this first we end up with [ other results, lst[0]) + move_to_end(blah, blah)
        # this allows us to preserve the order of the elements, but still move through the list
        # by slicing off each element per recursion
        result += move_to_end(lst[1:], val)

    return result


# Driver Code
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))

# result = [], ["Amber", "Sapphire", "Amber", "Jade"]
# PASS 1 val == lst[0]
#   [] += call(["Sapphire", "Amber", "Jade"])
# PASS 2 val != lst[0]
#   ["Sapphire"] += call(["Amber", "Jade"])
# PASS 3 val == lst[0]
#   [] += call(["Jade"])
# PASS 4 val != lst[0])
#   ["Jade"] + call(lst([]))
# PASS 5 BASE CASE return []
# PASS 4b
#   return ["Jade"] + []
# PASS 3b
#   return ["Jade"].append("Amber")
# PASS 2b
#   return ["Sapphire"] + ["Jade", "Amber"]
# PASS 1 (final result)
#   return ["Sapphire", "Jade", "Amber"].append("Amber")
