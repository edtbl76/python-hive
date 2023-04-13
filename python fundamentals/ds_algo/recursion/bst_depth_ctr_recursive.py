def depth(tree):
    if not tree:
        return 0

    # Calculate left and right paths recursively
    # whichever is longest wins
    left_depth = depth(tree['left_child'])
    right_depth = depth(tree['right_child'])
    print(f'R: {right_depth}, L: {left_depth}')
    # Python Ternary Operator - is stupid
    return left_depth + 1 if left_depth > right_depth else right_depth + 1
