#!/usr/bin/env python3

from math import inf
from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, thirty_sixth_and_sixth, grand_central_station, penn_station


# noinspection DuplicatedCode
def modified_dijkstras(graph, start, target):
    print("Starting Dijkstra's Algorithm")
    count = 0
    paths_and_distances = {}

    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

            if new_distance < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbor))
                count += 1
                print(f"\nAt {vertices_to_explore[0][1].name}")

    print(f'Found a path in {count} steps: {paths_and_distances[target][1]}')
    return paths_and_distances[target][1]


def heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance


# noinspection DuplicatedCode
def a_star(graph, start, target):
    print("Starting A* Algorithm")
    count = 0
    paths_and_distances = {}

    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]

    # The while loop does two things instead of 1
    # - like Dijkstra, it iterates through the neighbors
    # - we are looking only for paths that represent our selected destination (target)
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:

            # Our new_distance must also include a heuristic based on the adjacency and
            # our destination
            new_distance = current_distance + edge_weight + heuristic(neighbor, target)
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

            if new_distance < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbor))
                count += 1
                print(f"\nAt {vertices_to_explore[0][1].name}")

    print(f'Found a path in {count} steps: {paths_and_distances[target][1]}')
    return paths_and_distances[target][1]


# Drivah Cohde Kehd
modified_dijkstras(manhattan_graph, thirty_sixth_and_sixth, grand_central_station)

a_star(manhattan_graph, thirty_sixth_and_sixth, grand_central_station)
a_star(manhattan_graph, penn_station, grand_central_station)


