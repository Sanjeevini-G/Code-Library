def isSafe(vertex, color, graph, colors):
    for v in range(len(graph)):
        if graph[vertex][v] == 1 and colors[v] == color:
            return False
    return True

def backtrack(graph, colors, vertex):
    if vertex == len(graph):
        return True

    for color in range(1, max(colors) + 1):
        if isSafe(vertex, color, graph, colors):
            colors[vertex] = color
            if backtrack(graph, colors, vertex + 1):
                return True
            colors[vertex] = 0

    return False

n = int(input("Enter the number of vertices: "))
graph = []
for i in range(n):
    row = list(map(int, input(f"Enter the adjacency matrix row for vertex {i+1}: ").split()))
    graph.append(row)

colors = [0] * n
if backtrack(graph, colors, 0):
    print(f"Colors of vertices: {colors}")
else:
    print("No solution exists.")
