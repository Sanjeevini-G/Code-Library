from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def bfs(self, start):
        visited = [False] * (len(self.graph))
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for i in self.graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print("BFS traversal starting from vertex 2:")
g.bfs(2)
