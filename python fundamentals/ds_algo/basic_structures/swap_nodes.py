from linked_list import Node, LinkedList


def swap_nodes(input_list, value1, value2):
    print(f'Swapping {value1} with {value2}')

    node1_previous = None
    node2_previous = None
    node1 = input_list.get_head_node()
    node2 = input_list.get_head_node()


    # Edge Case - If the elements are the same, they don't need to be swapped
    if value1 == value2:
        print("Elements are equal, no swap needed.")
        return

    # Finding Matching and Preceding Nodes
    while node1 is not None:
        if node1.get_value() == value1:
            break
        node1_previous = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == value2:
            break
        node2_previous = node2
        node2 = node2.get_next_node()


    # Edge Case - No matching node for one of the inputs?
    if node1 is None or node2 is None:
        print("Swap isn't possible - one or more elements aren't in the list")
        return

    # Updating Preceding Nodes pointers
    if node1_previous is None:
        input_list.head_node = node2
    else:
        node1_previous.set_next_node(node2)

    if node2_previous is None:
        input_list.head_node = node1
    else:
        node2_previous.set_next_node(node1)

    # Updating Node's "Next" Pointers
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


# TEST CODE
def run():
    ll = LinkedList()
    for number in range(10):
        ll.insert_beginning(number)

    print(ll.stringify_list())
    swap_nodes(ll, 9, 5)
    print(ll.stringify_list())

if __name__ == '__main__':
    run()