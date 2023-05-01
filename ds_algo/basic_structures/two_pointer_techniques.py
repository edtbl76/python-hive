def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
    return current


# find middle
def find_middle(linked_list):
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow


# This is half as fast as the previous, because it only moves the slow pointer once every-other iteration
def find_middle_alt(linked_list):
    count = 0
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if count % 2 != 0:
            slow = slow.get_next_node()
        count += 1
    return slow
