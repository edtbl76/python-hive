#!/usr/bin/env python3
from vertex import Vertex
from graph import Graph

# - Testing Add Edges (Undirected)
railway = Graph()

station_one = Vertex("Lowell")
station_two = Vertex("Worcester")

railway.add_vertex(station_one)
railway.add_vertex(station_two)

railway.add_edge(station_one, station_two)
print(f'Edges for {station_one.value}: {station_one.get_edges()}')
print(f'Edges for {station_two.value}: {station_two.get_edges()}')