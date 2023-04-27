#!/usr/bin/env python
from __future__ import print_function

# Data Structure
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    # Methods For Adding Nodes
    def add_to_head(self, data):
        self.head = Node(data=data, next_node=self.head)

    def add_to_tail(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data=data)


    # Methods for Destroying Nodes
    def delete_node(self, key):
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if not previous:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None

    # Query Methods
    def get_last_node(self):
        ph = self.head
        while(ph.next):
            ph = ph.next
        return ph.data

    def output(self):
        n = self.head
        while n:
            print(n.data, end=" => ")
            n = n.next


    # Verification Methods
    def is_empty(self):
        return self.head is None




# Demo Code
def main():
    s = LinkedList()

    # Show No Output
    s.output()
    print()

    # Add Some Stuff and show output
    s.add_to_tail(5)
    s.add_to_head(3)
    s.add_to_tail(4)
    s.output()
    print()

    # Show last node
    print(s.get_last_node())

    # Delete Something and show the result.
    s.delete_node(5)
    s.output()



if __name__ == '__main__':
    main()

