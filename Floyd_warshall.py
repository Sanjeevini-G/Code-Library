INF = float("inf")

def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [[0, INF, 3, INF], [2, 0, INF, INF], [INF, 7, 0, 1], [6, INF, INF, 0]]
dist = floyd_warshall(graph)
for row in dist:
    print(row)
