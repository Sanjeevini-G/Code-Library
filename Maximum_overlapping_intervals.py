def findMaxOverlap(intervals):
    maxOverlap = 0
    currentOverlap = 0

    points = []
    for start, end in intervals:
        points.append((start, 1))
        points.append((end, -1))

    points.sort()

    for _, delta in points:
        currentOverlap += delta
        maxOverlap = max(maxOverlap, currentOverlap)

    return maxOverlap

n = int(input("Enter the number of intervals: "))
intervals = []
for i in range(n):
    start, end = map(int, input(f"Enter the start and end of interval {i+1}: ").split())
    intervals.append((start, end))

maxOverlap = findMaxOverlap(intervals)
print(f"Maximum overlap: {maxOverlap}")
