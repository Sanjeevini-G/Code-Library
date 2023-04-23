def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)

    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    for i in range(len(arr)):
        buckets[(arr[i] - min_value) // bucket_size].append(arr[i])

    result = []
    for i in range(bucket_count):
        buckets[i].sort()
        for j in range(len(buckets[i])):
            result.append(buckets[i][j])

    return result

# Example usage of bucket sort
arr = [8, 2, 3, 5, 1, 9, 4, 6, 7]
sorted_arr = bucket_sort(arr)
print(sorted_arr)    # prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
