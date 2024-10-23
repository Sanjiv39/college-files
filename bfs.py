from collections import deque


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])
            graph = {
                'A': ['B', 'C'],
                'B': ['D', 'E'],
                'C': ['F'],
                'D': [],
                'E': ['F'],
                'F': []
            }
    bfs(graph, 'A')
