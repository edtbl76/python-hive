#!/usr/bin/env python3

import random
from random import randrange
from Graph import Graph
from Vertex import Vertex


def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(f'{vertex} connected to ')
        neighbors = graph.graph_dict[vertex].edges
        if len(neighbors) == 0:
            print("No edges!")
        for adjacency in neighbors:
            print(f'=> {adjacency}')


# Traveling Salesperson problem requires a
# connected graph w/ symmetrical weights.
def build_traveling_salesperson_path(directed):
    graph = Graph(directed)
    vertices = []
    for value in ['a', 'b', 'c', 'd']:
        vertex = Vertex(value)
        vertices.append(vertex)
        graph.add_vertex(vertex)

    graph.add_edge(vertices[0], vertices[1], 3)
    graph.add_edge(vertices[0], vertices[2], 4)
    graph.add_edge(vertices[0], vertices[3], 5)
    graph.add_edge(vertices[1], vertices[0], 3)
    graph.add_edge(vertices[1], vertices[2], 2)
    graph.add_edge(vertices[1], vertices[3], 6)
    graph.add_edge(vertices[2], vertices[0], 4)
    graph.add_edge(vertices[2], vertices[1], 2)
    graph.add_edge(vertices[2], vertices[3], 1)
    graph.add_edge(vertices[3], vertices[0], 5)
    graph.add_edge(vertices[3], vertices[1], 6)
    graph.add_edge(vertices[3], vertices[2], 1)
    return graph


def visited_all_nodes(visited_vertices):
    for vertex in visited_vertices:
        if visited_vertices[vertex] == 'unvisited':
            return False

    return True


# Main Driver Method
def traveling_salesperson(graph):
    sales_route = ""

    visited_vertices = {vertex: "unvisited" for vertex in graph.graph_dict}
    current_vertex = random.choice(list(graph.graph_dict))
    visited_vertices[current_vertex] = 'visited'
    sales_route += current_vertex

    has_visited_all_vertices = visited_all_nodes(visited_vertices)
    while not has_visited_all_vertices:
        current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
        current_vertex_edge_weights = {}
        for edge in current_vertex_edges:
            current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)

            found_next_vertex = False
            next_vertex = ""

            while not found_next_vertex:
                if len(current_vertex_edge_weights) == 0:
                    break

                next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
                if visited_vertices[next_vertex] == 'visited':
                    current_vertex_edge_weights.pop(next_vertex)
                else:
                    found_next_vertex = True


            if current_vertex_edge_weights is None:
                has_visited_all_vertices = True
            else:
                current_vertex = next_vertex
                visited_vertices[next_vertex] = 'visited'
                sales_route += current_vertex


        has_visited_all_vertices = visited_all_nodes(visited_vertices)

    print(sales_route)


    

graph = build_traveling_salesperson_path(False)
traveling_salesperson(graph)