from TreeNode_dfs import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)
#   A
#   |-B
#   | |-D
#   | |-E
#   |-C
#   | |-F
#   | _-G


def dfs(root, target, path):

    path = path + (root,)
    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None


# Driver Code
print(dfs(sample_root_node, "F"))