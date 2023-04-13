#!/usr/bin/env python3

def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []
    print(f'Current Vertex: {current_vertex}')
    print(f'Visited       : {visited}')
    visited.append(current_vertex)
    if current_vertex is target_value:
        print(f'Found Target! : {current_vertex}')
        return visited

    for neighbor in graph[current_vertex]:
        print(f'Neighbor: {neighbor}')
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)
            if path:
                return path



some_important_graph = {
    'lava': {'sharks', 'piranhas'},
    'sharks': {'lava', 'bees', 'lasers'},
    'piranhas': {'lava', 'crocodiles'},
    'bees': {'sharks'},
    'lasers': {'sharks', 'crocodiles'},
    'crocodiles': {'piranhas', 'lasers'}
  }

print(dfs(some_important_graph, 'lava', 'lasers'))

