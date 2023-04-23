import sys
sys.setrecursionlimit(1000000)

mod = 1000000007

def dfs(node, parent):
    subtree_size[node] = 1
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            subtree_size[node] += subtree_size[child]
            node_contrib[node] += node_contrib[child] + subtree_size[child]

def solve(u, v, x, y):
    # case 1: x is ancestor of y
    if x == u and y == v:
        return (n - subtree_size[x]) * subtree_size[x]
    
    # case 2: y is ancestor of x
    if y == u and x == v:
        return (n - subtree_size[y]) * subtree_size[y]
    
    # case 3: u is ancestor of x and v is ancestor of y
    if x == u and y == v:
        return node_contrib[y] * (n - subtree_size[x]) + subtree_size[x] * (n - subtree_size[y])
    
    # case 4: u is ancestor of y and v is ancestor of x
    if y == u and x == v:
        return node_contrib[x] * (n - subtree_size[y]) + subtree_size[y] * (n - subtree_size[x])
    
    # case 5: none of the above cases apply
    if (x == u or x == v) and (y == u or y == v):
        return node_contrib[x] * (n - subtree_size[y]) + node_contrib[y] * (n - subtree_size[x])
    
    # case 6: u and v are both ancestors of x and y, but not in the same path
    return subtree_size[x] * subtree_size[y]

# main function
for _ in range(int(input())):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    subtree_size = [0] * (n+1)
    node_contrib = [0] * (n+1)
    
    for i in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    
    dfs(1, 0)
    
    ans = 0
    for u in range(2, n+1):
        for v in tree[u]:
            if v == 1 or v == u:
                continue
            for x in range(1, u):
                for y in tree[x]:
                    if y == 1 or y == x:
                        continue
                    ans = (ans + solve(u, v, x, y)) % mod
    
    print(ans)
