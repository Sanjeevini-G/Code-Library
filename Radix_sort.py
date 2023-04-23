def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        buckets = [[] for _ in range(10)]
        for i in range(len(arr)):
            buckets[(arr[i] // exp) % 10].append(arr[i])
        arr = []
        for bucket in buckets:
            for i in range(len(bucket)):
                arr.append(bucket[i])
        exp *= 10

    return arr

# Example usage of radix sort
arr = [8, 2, 3, 5, 1, 9, 4, 6, 7]
sorted_arr = radix_sort(arr)
print(sorted_arr)    # prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
