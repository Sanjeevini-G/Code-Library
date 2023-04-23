import heapq

def prim(graph):
    visited = set()
    start_vertex = list(graph.keys())[0]
    heap = [(0, start_vertex)]
    mst_cost = 0
    mst_edges = []
    while heap:
        cost, current_vertex = heapq.heappop(heap)
        if current_vertex not in visited:
            visited.add(current_vertex)
            mst_cost += cost
            if cost != 0:
                mst_edges.append((cost, current_vertex))
            for neighbor, weight in graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap, (weight, neighbor))
    return mst_cost, mst_edges

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
mst_cost, mst_edges = prim(graph)
print("The cost of the minimum spanning tree is:", mst_cost)
print("The edges in the minimum spanning tree are:")
for cost, vertex in mst_edges:
    print(f"{vertex} -- {cost} --> {graph[vertex][0][0]}")
