#!/usr/bin/env python3
from vertex import Vertex
from graph import Graph

no_path_exists = True

directed_railway = Graph(True)

# noinspection DuplicatedCode
north_station = Vertex("North Station")
west_medford = Vertex("West Medford")
wedgemere = Vertex("Wedgemere")
anderson = Vertex("Anderson/Woburn")
wilmington = Vertex("Wilmington")
north_billerica = Vertex("North Billerica")
lowell = Vertex("Lowell")

directed_railway.add_vertex(north_station)
directed_railway.add_vertex(west_medford)
directed_railway.add_vertex(wedgemere)
directed_railway.add_vertex(anderson)
directed_railway.add_vertex(wilmington)
directed_railway.add_vertex(north_billerica)
directed_railway.add_vertex(lowell)

directed_railway.add_edge(north_station, west_medford)
directed_railway.add_edge(west_medford, wedgemere)
directed_railway.add_edge(wedgemere, anderson)
directed_railway.add_edge(anderson, wilmington)
directed_railway.add_edge(wilmington, north_billerica)
directed_railway.add_edge(north_billerica, lowell)

path_exists = directed_railway.find_path('North Billerica', 'North Billerica')
print(path_exists)


print("\n\n\nFinding path from North Station to Lowell\n")
new_path_exists = directed_railway.find_path('North Station', 'Lowell')
print(new_path_exists)
print("\n\nTrying to find path from Lowell to North Station\n")
no_path_exists = directed_railway.find_path('Lowell', 'North Station')
print(no_path_exists)