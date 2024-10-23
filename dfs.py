graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(graph, node, visited):
    if node not in visited:
        print(node)  # Visit the node
        visited.add(node)  # Mark the node as visited
        for neighbor in graph[node]:  # Recur for all the neighbors
            dfs(graph, neighbor, visited)
            visited = set()  # Set to keep track of visited nodes
            dfs(graph, 'A', visited)
