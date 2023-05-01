#!/usr/bin/env python3

from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


# Define dijkstras() below:
def dijkstras(graph, start):
    # Set up an empty dictionary to store shortest paths
    distances = {}

    # Iterate through each vertex, and seed the shortest path structure
    # with infinite paths as a starting point
    for vertex in graph:
        distances[vertex] = inf

    # Set distances to the provided starting point to 0 (because that's the starting point)
    distances[start] = 0

    # Create a list of tuples (weight, vertex) to inspect. We'll begin with the provided 'start'
    vertices_to_explore = [(0, start)]

    # Loop through our list of tuples.
    while vertices_to_explore:
        # Use parallel assignment to get the distance and vertex.
        # - pop the value off of the list so we don't explore it twice.
        current_distance, current_vertex = heappop(vertices_to_explore)

        # Plug the current_vertex into the provided graph
        #   - loop through it's associated adjacency list and weights.
        for neighbor, edge_weight in graph[current_vertex]:

            # add the weight of the neighbor to our current_distance from the 'vertices to explore'
            new_distance = current_distance + edge_weight

            # compare the calculated value to any existing distance in the shortest_distance table.
            # (We only care about shorter distances)
            if new_distance < distances[neighbor]:
                # if the newly calculated value is different, replace that value in the shortest distance table
                distances[neighbor] = new_distance

                # add the neighbor vertex to the vertices_to_explore
                heappush(vertices_to_explore, (new_distance, neighbor))

    # once the while loop is exhausted, we can return the shortest distance table.
    return distances


# Driver Code
distances_from_d = dijkstras(graph, 'D')
print(f"\n\nShortest Distances: {distances_from_d}")