#!/usr/bin/env python3
from vertex import Vertex
from graph import Graph


# Example 1
# - Testing Vertex
grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

print(grand_central.get_edges())
grand_central.add_edge(forty_second_street.value)

print(grand_central.get_edges())

# - Testing Graph
railway = Graph()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)




# Example 3
# Testing Weights
