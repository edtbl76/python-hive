# Define build_bst() below...
def build_bst(my_list):
    # Base Case
    if len(my_list) == 0:
        return "No Child"

    # Recursive Step remove element from input
    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
    print(f"Middle Index: {middle_idx}")
    print(f"Middle Value: {middle_value}")

    # Represents the tree being created in this
    # function call.
    #
    # We create a tree_node for each element in the
    # list, so it is repeated on the left/right subtrees
    # on the approp. half of the list.
    tree_node = {"data": middle_value}

    # Excluse the middle value in order to avoid
    # creating duplicate nodes.
    tree_node['left_child'] = build_bst(my_list[:middle_idx])
    tree_node['right_child'] = build_bst(my_list[middle_idx + 1:])
    return tree_node


# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"