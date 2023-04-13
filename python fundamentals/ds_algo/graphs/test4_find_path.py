#!/usr/bin/env python3
from vertex import Vertex
from graph import Graph

undirected_railway = Graph()

north_station = Vertex("North Station")
west_medford = Vertex("West Medford")
wedgemere = Vertex("Wedgemere")
anderson = Vertex("Anderson/Woburn")
wilmington = Vertex("Wilmington")
north_billerica = Vertex("North Billerica")
lowell = Vertex("Lowell")

undirected_railway.add_vertex(north_station)
undirected_railway.add_vertex(west_medford)
undirected_railway.add_vertex(wedgemere)
undirected_railway.add_vertex(anderson)
undirected_railway.add_vertex(wilmington)
undirected_railway.add_vertex(north_billerica)
undirected_railway.add_vertex(lowell)

undirected_railway.add_edge(north_station, west_medford)
undirected_railway.add_edge(west_medford, wedgemere)
undirected_railway.add_edge(wedgemere, anderson)
undirected_railway.add_edge(anderson, wilmington)
undirected_railway.add_edge(wilmington, north_billerica)
undirected_railway.add_edge(north_billerica, lowell)

undirected_railway.find_path('North Billerica', 'Lowell')

