from collections import deque

def bfs(x, y, z):
    q = deque()
    visited = set()

    q.append((0, 0))

    while q:
        j1, j2 = q.popleft()

        if (j1, j2) in visited:
            continue

        visited.add((j1, j2))

        if j1 == z or j2 == z or j1 + j2 == z:
            return True

        q.append((x, j2))
        q.append((j1, y))
        q.append((0, j2))
        q.append((j1, 0))

        if j1 + j2 <= y:
            q.append((0, j1 + j2))
        else:
            q.append((j1 - (y - j2), y))

        if j1 + j2 <= x:
            q.append((j1 + j2, 0))
        else:
            q.append((x, j2 - (x - j1)))

    return False

x, y, z = map(int, input("Enter the sizes of the jugs and the desired amount of water: ").split())

if bfs(x, y, z):
    print("It is possible to measure the desired amount of water.")
else:
    print("It is not possible to measure the desired amount of water.")
