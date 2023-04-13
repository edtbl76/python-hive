from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print(f'Adding {vertex.value}')
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        print(f'Adding edge from {from_vertex.value} to {to_vertex.value}')
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        print(f'Searching for a path from {start_vertex} to {end_vertex}')
        start = [start_vertex]

        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)

            # Mark visited
            seen[current_vertex] = True
            print(f'Visiting {current_vertex}')

            if current_vertex == end_vertex:
                return True

            vertex = self.graph_dict[current_vertex]
            next_vertices = vertex.get_edges()
            # Avoid duplicates by ensuring that we only show unique vertices
            next_vertices = [vertex for vertex in next_vertices if vertex not in seen]

            # more elegant than start += next_vertices
            start.extend(next_vertices)
        return False




