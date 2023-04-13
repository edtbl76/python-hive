#! /usr/bin/env python3

######
# TREENODE CLASS
######
class TreeNode:
    def __init__(self, story_segment):
        self.story_segment = story_segment
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_segment)

        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice not in ['1', '2']:
                print("Invalid Choice. Try Again")
            else:
                # Convert input to int and adjust
                # for 0 index
                chosen_index = int(choice) - 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_segment)
                story_node = chosen_child


######
# VARIABLES FOR TREE
######
story_root = TreeNode("""
You are in a forest clearning. There is a path
to the left.
A bear emerges from the trees and roars!
Do you:
1. Roar Back!
2. Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1. Shout 'Sorry Bear!'
2. Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come acress a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1. Gasp 'A talking bear!'
2. Explain that the bear scared you.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode("""
The bear returns and tells you it's been
a rough week. After making peace with a 
talking bear, he shows you the way out of 
the forest.

YOU HAVE ESCAPED THE WILDNERNESS
""")
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# TESTING AREA
######
name = input("Please enter your name: ")
print(f'{name} welcome to Escape The Wilderness...\n\n\n')
print("Once upon a time...")
story_root.traverse()
