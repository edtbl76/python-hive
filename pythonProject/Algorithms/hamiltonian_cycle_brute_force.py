class Hamiltonian:
    def __init__(self, vertices, adjacency_matrix, starting_vertex):
        # Store the vertices
        self.vertices = vertices

        # Store the adjacency matrix
        self.adj_matrix = adjacency_matrix

        # Store the starting vertex
        self.start = starting_vertex

        # Create a list to hold the current path
        self.path = []

        # Create a list to hold all visited vertices, where
        # 0 means not visited, and 1 means visited.
        # To start out, all vertices are 0.
        self.visited_vertices = [0 for x in range(len(self.vertices))]

        # Create list for all Hamiltonian paths
        self.hpaths = []

        # Create a list that stores all Hamiltonian cycles
        self.cycles = []

        self.num_vertices = len(self.vertices)

    def traverse(self):
        # Add the starting vertex to the path list
        self.path.append(self.start)

        # start the recursive search on the first vertex to find the path and cycle if they exist
        self.search(self.start)

    def search(self, vertex):
        # First check for exit condition
        # Have all vertices been visited
        all_visited = True
        for i in range(1, len(self.visited_vertices)):
            if self.visited_vertices[i] == 0:
                all_visited = False
                break

        # Ensure that every vertex was visited and that there are no duplicate
        # visited vertices -> This is a Hamiltonian path
        if all_visited and len(self.path) == len(set(self.path)):
            # append the path to the hpaths list
            # Since th epath variable will be modified, create a deep copy of the list
            # before appending it
            self.hpaths.append(list(self.path))

        # Check for cycles
        # if current vertex equals the starting vertex AND the path length equals the number of vertexes
        # pus one (since the starting node is always in the path twice)
        if vertex == self.start and len(self.path) == self.num_vertices + 1:
            # Append path to cycles list.
            # Since path variable will be modified, create a deep copy of the list before appending it
            self.cycles.append(list(self.path))

            return

        # loop through vertices
        for neighbor in range(len(vertices)):
            # check if neighbor is connected to vertex and hasn't been previously
            # visited
            if self.adj_matrix[vertex][neighbor] == 1 and self.visited_vertices[neighbor] == 0:
                # set this neighbor index within visited_vertices to 1
                self.visited_vertices[neighbor] = 1

                # add the neighbor to the path
                self.path.append(neighbor)

                # Traverse the neighbor to continue finding the path
                self.search(neighbor)

                # Backtrack (for failed paths)
                # Set the neighbor index in visited_vertices back to 0
                self.visited_vertices[neighbor] = 0

                # Pop the neighbor from the path
                self.path.pop()


# Driver Code
vertices = ['School', 'Sanjay', 'Marquis', 'Marisol', 'Lisa']
adjacency_matrix = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]
ham = Hamiltonian(vertices, adjacency_matrix, 0)
ham.traverse()
print("Hamiltonian paths:" + str(ham.hpaths))
print("Hamiltonian cycles:" + str(ham.cycles))
