#!/usr/bin/env python3

def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()

    print(f'Path            : {path}')
    print(f'Vertex and Path : {vertex_and_path}')
    print(f'BFS Queue       : {bfs_queue}')
    print(f'Visited Set     : {visited}')
    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        print(f'[WHILE] Current Vertex  : {current_vertex}')
        print(f'[WHILE] Path            : {path}')
        visited.add(current_vertex)
        print(f'[WHILE] Visited Set     : {visited}')

        for neighbor in graph[current_vertex]:
            print(f'[FOR] Neighbor: {neighbor}')
            if neighbor not in visited:
                if neighbor is target_value:
                    print(f"Found Target! {path + [neighbor]}")
                    return path + [neighbor]
                else:
                    print(f"Adding {neighbor}")
                    bfs_queue.append([neighbor, path + [neighbor]])
            else:
                print(f'Already visited {neighbor}')

        print(f'[AFTER FOR] BFS QUEUE: {bfs_queue}')


# def dfs(graph, current_vertex, target_value, visited=None):
#     if visited is None:
#         visited = []
#
#     visited.append(current_vertex)
#     if current_vertex is target_value:
#         return visited
#
#     for neighbor in graph[current_vertex]:
#         if neighbor not in visited:
#             path = dfs(graph, neighbor, target_value, visited)
#             if path:
#                 return path



some_important_graph = {
    'lava': {'sharks', 'piranhas'},
    'sharks': {'lava', 'bees', 'lasers'},
    'piranhas': {'lava', 'crocodiles'},
    'bees': {'sharks'},
    'lasers': {'sharks', 'crocodiles'},
    'crocodiles': {'piranhas', 'lasers'}
  }

print(bfs(some_important_graph, 'lava', 'lasers'))
# print(dfs(some_important_graph, 'lava', 'lasers'))

