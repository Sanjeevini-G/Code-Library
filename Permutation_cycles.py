def find_cycles(perm):
    n = len(perm)
    visited = [False] * n
    cycles = []
    
    for i in range(n):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                cycle.append(j + 1)
                visited[j] = True
                j = perm[j] - 1
            cycle.append(j + 1)
            cycles.append(cycle)
    
    return cycles


# Read input
n = int(input())
perm = list(map(int, input().split()))

# Find cycles
cycles = find_cycles(perm)

# Print output
print(len(cycles))
for cycle in cycles:
    print(" ".join(map(str, cycle)))
