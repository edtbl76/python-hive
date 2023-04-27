#!/usr/bin/env python

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        """
                This is functionally identical to py2_queue.py w/ the exception of how lists use the *.pop() method.
                The default behavior for pop is to take the last item off of the list. py2_queue.py uses the default
                behavior to preserve the FIFO nature of a queue.
        """
        return self.items.pop(0)

    def dumpStack(self):
        print(self.items)


def main():
    s = Stack()

    # Show Nothing
    s.dumpStack()

    # add some stuff and show it again
    s.push('a')
    s.push('b')
    s.push('c')
    s.dumpStack()

    # rip the top off and print it again
    s.pop()
    s.dumpStack()


if __name__ == '__main__':
    main()