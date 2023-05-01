#!/usr/bin/env python3
from vertex import Vertex
from graph import Graph

railway = Graph()

boston = Vertex('Boston')
lowell = Vertex('Lowell')
worcester = Vertex('Worcester')

railway.add_vertex(boston)
railway.add_vertex(lowell)
railway.add_vertex(worcester)

railway.add_edge(boston, lowell, 12)
railway.add_edge(worcester, lowell, 7)
railway.add_edge(boston, worcester)

print(boston.edges)
print(lowell.edges)
print(worcester.edges)
