# ITERATIVE
def depth(tree):
    result = 0

    # Q will store nodes at each level
    queue = [tree]

    # loop as long as we have nodes.
    while queue:
        # count no. of child nodes
        children = len(queue)

        for child_count in range(0, children):
            # loop through each child
            child = queue.pop()

            # add existing children
            if child['left_child']:
                queue.append(child['left_child'])
            if child['right_child']:
                queue.append(child['right_child'])

        # incr level
        result += 1
    return result


# Driver Code
two_level_tree = {
    "data": 6,
    "left_child":
        {"data": 2}
}

four_level_tree = {
    "data": 54,
    "right_child":
        {"data": 93,
         "left_child":
             {"data": 63,
              "left_child":
                  {"data": 59}
              }
         }
}

depth(two_level_tree)
# 2
depth(four_level_tree)


# 4


# ITERATIVE
def depth_with_comments(tree):
    result = 0

    # Q will store nodes at each level
    queue = [tree]
    print(f'Queue: {queue}')

    # loop as long as we have nodes.
    while queue:
        # count no. of child nodes
        children = len(queue)

        for _ in range(0, children):
            # loop through each child
            child = queue.pop()
            print(f'Child: {child}')
            # add existing children
            if child['left_child']:
                print(f"### Found LEFT CHILD: {child['left_child']}")
                queue.append(child['left_child'])
            if child['right_child']:
                print(f"### Found RIGHT CHILD: {child['right_child']}")
                queue.append(child['right_child'])
            print(f'Queue After Append: {queue}')
        # incr level
        result += 1
        print(f'Result: {result}')
    return result
