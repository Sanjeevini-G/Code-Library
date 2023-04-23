def knightMoves(src, dest):
    n = 8
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    queue = [(src[0]-1, src[1]-1, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[src[0]-1][src[1]-1] = True
    while queue:
        x, y, dist = queue.pop(0)
        if x == dest[0]-1 and y == dest[1]-1:
            return dist
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))

src = (1, 1)
dest = (8, 8)
print(knightMoves(src, dest))  # Output: 6
