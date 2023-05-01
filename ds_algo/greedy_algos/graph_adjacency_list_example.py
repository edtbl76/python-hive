#!/usr/bin/env python3

graph = {
    'A': [('B', 10), ('C', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('B', 15)]
}

for vertex in graph:
    print("\n\nVertex {vertex} connects to")
    for edge in graph[vertex]:
        print('vertex {edge[0]} with a weight of {edge[1]}')
