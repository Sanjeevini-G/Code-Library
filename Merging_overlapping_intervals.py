def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
    return merged_intervals

n = int(input("Enter the number of intervals: "))
intervals = []

for i in range(n):
    start, end = map(int, input("Enter the start and end times of interval {}: ".format(i+1)).split())
    intervals.append([start, end])

merged_intervals = merge_intervals(intervals)

print("Merged intervals:")
for interval in merged_intervals:
    print(interval[0], interval[1])
