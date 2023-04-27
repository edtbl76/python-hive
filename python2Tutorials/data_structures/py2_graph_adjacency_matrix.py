#!/usr/bin/env python
from __future__ import print_function

""" This is an example of an adjacency matrix implemented using a graph data structure. 
    This is probably the most common example of a graph
"""

class Graph:
    def __init__(self, size):
        self.adjacent = []
        for i in range(1, size+1):
            self.adjacent.append([ 0 for i in range(size)])
        self.size = size

    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Trying to add an invalid edge ({} {})".format(orig, dest))
        else:
            self.adjacent[orig-1][dest-1] = 1
            self.adjacent[dest-1][orig-1] = 1

    def remove_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Trying to remove an invalid edge ({} {})".format(orig, dest))
        else:
            self.adjacent[orig - 1][dest - 1] = 0
            self.adjacent[dest - 1][orig - 1] = 0

    def display(self):
        for row in self.adjacent:
            print()
            for value in row:
                print('{:4}'.format(value), end="")

def main():
    g = Graph(7)

    g.add_edge(5,5)
    g.add_edge(1,5)
    g.add_edge(5,1)
    g.add_edge(3,3)
    g.add_edge(7,3)

    g.display()

if __name__ == '__main__':
    main()