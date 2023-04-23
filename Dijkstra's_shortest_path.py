import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor] and neighbor not in visited:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

n = int(input("Enter the number of vertices: "))
graph = {}
for i in range(n):
    edges = []
    while True:
        line = input(f"Enter the edges connected to vertex {i+1} (enter -1 to stop): ")
        if line == "-1":
            break
        neighbor, weight = map(int, line.split())
        edges.append((neighbor, weight))
    graph[i+1] = edges
