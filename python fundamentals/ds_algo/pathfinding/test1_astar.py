#!/usr/bin/env python3

from math import inf
from heapq import heappop, heappush


# A difference between Dijkstra and A* is that
# A* requires a clearly defined destination 'target'.
def a_star(graph, start, target):
    # Create an empty dict to store paths and distances
    paths_and_distances = {}

    # Loop through the vertex in the graph to seed our paths/distances table
    for vertex in graph:
        # for each vertex, we want to set the distance to infinite, and the path equal to the vertex name
        # we'll append to the vertex name to build the path.
        paths_and_distances[vertex] = [inf, [start.name]]

    # Just like Dijkstra
    # - we want to update the distance to 0 for the startpoint.
    # - and we'll initiate a staging ground structure (the list) w/ the initial distance and vertex.
    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]

    # Loop through the staging list to investigate adjacencies.
    while vertices_to_explore:
        # Get the distance and vertex of the current vertex.
        # - make sure to remove the value from our staging list to avoid inspecting it twice.
        current_distance, current_vertex = heappop(vertices_to_explore)

        # loop through the elements (vertex name and weight respectivelhy)  of the neighbor list of the current vertex,
        # by 'getting' it from the graph
        for neighbor, edge_weight in graph[current_vertex]:
            # calculate the distance by adding the weight of the neighbor to the current distance
            new_distance = current_distance + edge_weight

            # A star also builds a path by appending the neighbor name to the current vertex name.
            # (This ensures that we are moving towards the destination as opposed to moving outward in every
            # direction from the starting point)
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
            if new_distance < paths_and_distances[neighbor][0]:

                # If the new distance is shorter then we need to update our paths/distances w/ the new distance and path
                # for that NEIGHBOR.
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path

                # Once the values are updated, we need to add the neighbor to the paths/distances structure
                heappush(vertices_to_explore, (new_distance, neighbor))

    # Once the staging list is exhausted, we can return our result.
    return paths_and_distances[target][1]


# Driver Code


# A graph and vertices for us to play around with:
class graphVertex:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)


delhi = graphVertex("New Delhi", 28.6448, 77.216721)
jaipur = graphVertex("Jaipur", 26.92207, 75.778885)
varanasi = graphVertex("Varanasi", 25.321684, 82.987289)
mumbai = graphVertex("Mumbai", 19.07283, 72.88261)
chennai = graphVertex("Chennai", 13.067439, 80.237617)
hyderabad = graphVertex("Hyderabad", 17.387140, 78.491684)
kolkata = graphVertex("Kolkata", 22.572645, 88.363892)
bengaluru = graphVertex("Bengaluru", 12.972442, 77.580643)

cities_graph = {
    delhi: {(jaipur, 2.243918), (varanasi, 6.65902), (mumbai, 10.507479), (chennai, 15.867576), (hyderabad, 11.329626),
            (kolkata, 12.693718), (bengaluru, 15.676582)},
    jaipur: {(mumbai, 8.366539), (delhi, 2.243918)},
    varanasi: {(delhi, 6.65902), (mumbai, 11.88077)},
    mumbai: {(delhi, 10.507479), (jaipur, 8.366539), (varanasi, 11.88077), (hyderabad, 5.856898), (kolkata, 15.87195),
             (bengaluru, 7.699756)},
    chennai: {(delhi, 15.867576), (kolkata, 12.50541), (hyderabad, 4.659195), (bengaluru, 2.658671)},
    hyderabad: {(delhi, 11.329626), (mumbai, 5.856898), (chennai, 4.659195), (bengaluru, 4.507721),
                (kolkata, 11.151231)},
    kolkata: {(delhi, 12.693718), (mumbai, 15.87195), (chennai, 12.50541), (hyderabad, 11.151231),
              (bengaluru, 14.437532)},
    bengaluru: {(delhi, 15.676582), (mumbai, 7.699756), (chennai, 2.658671), (hyderabad, 4.507721),
                (kolkata, 14.437532)}
}
a_star(cities_graph, delhi, varanasi)
