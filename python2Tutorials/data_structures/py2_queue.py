#!/usr/bin/env python

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        """
        This is functionally identical to py2_stack.py w/ the exception of how lists use the *.pop() method.
        The default behavior for pop is to take the last item off of the list. py2_stack.py works around this by
        providing the index of the first item to ensure the LIFO nature of Stacks.
        """
        return self.items.pop()

    def dump(self):
        print(self.items)


def main():
    q = Queue()

    # Show Nothing
    q.dump()

    # add some stuff and show it again
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('42')
    q.dump()

    # remove the first one in
    q.dequeue()
    q.dump()


if __name__ == '__main__':
    main()