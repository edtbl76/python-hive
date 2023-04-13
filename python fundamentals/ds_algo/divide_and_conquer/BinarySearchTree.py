#!/usr/bin/env python3

class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        # Left search
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'TreeNode {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        # right Search
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'TreeNode {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        # HIT
        if value == self.value:
            return self
        # LEFT SIDE
        elif self.left and value < self.value:
            return self.left.get_node_by_value(value)
        # RIGHT SIDE
        elif self.right and value < self.value:
            return self.right.get_node_by_value(value)
        # NOT FOUND
        else:
            return None

    def depth_first_traversal(self):
        # In order Traversal

        # Left
        if self.left:
            self.left.depth_first_traversal()

        # 'Current'
        print(f'Depth={self.depth}, Value={self.value}')

        # Right
        if self.right:
            self.right.depth_first_traversal()


# Example 1
# # Create a new BST:
# root = BinarySearchTree(15)
#
# # Print root's value below:
# print(root.value)


# Example 2 - INSERTION and GET NODE BY VALUE
# root = BinarySearchTree(100)
#
# # Insert values below:
# root.insert(50)
# root.insert(125)
# root.insert(75)
# root.insert(25)
#
# # Get nodes by value below:
# print(root.get_node_by_value(75).value)
# print(root.get_node_by_value(55))

# Example 3 - DFS - Inorder
tree = BinarySearchTree(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)

# Print depth-first traversal:
tree.depth_first_traversal()