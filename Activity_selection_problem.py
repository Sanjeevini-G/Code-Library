def activitySelection(start, end):
    n = len(start)
    selected = []

    i = 0
    selected.append(i)

    for j in range(1, n):
        if start[j] >= end[i]:
            selected.append(j)
            i = j

    return selected

n = int(input("Enter the number of activities: "))
start = []
end = []

for i in range(n):
    s, e = map(int, input(f"Enter the start and end time for activity {i+1}: ").split())
    start.append(s)
    end.append(e)

selected = activitySelection(start, end)

print("Selected activities:", selected)
