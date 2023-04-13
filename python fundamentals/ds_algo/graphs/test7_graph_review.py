#! /usr/bin/env python3

from random import randrange
from graph import Graph
from vertex import Vertex


def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(f'{vertex} is connected to')
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print(" no edges!")

        for adjacent_vertex in vertex_neighbors:
            print(f" => {adjacent_vertex}")


def build_graph(directed):
    graph = Graph(directed)
    vertices = []
    for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        vertex = Vertex(val)
        vertices.append(vertex)
        graph.add_vertex(vertex)

    for val in range(len(vertices)):
        value_index = randrange(0, len(vertices) - 1)
        value1 = vertices[value_index]

        value_index = randrange(0, len(vertices) - 1)
        value2 = vertices[value_index]
        graph.add_edge(value1, value2, randrange(1, 10))

    print_graph(graph)


build_graph(False)