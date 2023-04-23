class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, u, v):
        u_root = self.find(parent, u)
        v_root = self.find(parent, v)
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
            
    def kruskal(self):
        result = []
        i = 0
        e = 0
        self.edges = sorted(self.edges, key=lambda x: x[2])
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices-1:
            u, v, w
