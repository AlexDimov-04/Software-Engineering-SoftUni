def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def unreachable_outposts(N, edges, start_node):
    graph = {i: [] for i in range(1, N + 1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])

    visited = []
    dfs(graph, start_node, visited)

    unreachable = [i for i in range(1, N + 1) if i not in visited]
    return unreachable

n, m = int(input()), int(input())

edges = []

for _ in range(m):
    edge = tuple(map(int, input().split()))
    edges.append(edge)

start_node = int(input())

print(*unreachable_outposts(n, edges, start_node))
