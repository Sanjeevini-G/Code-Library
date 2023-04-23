def k_partition(arr, k):
    n = len(arr)
    s = sum(arr)
    if s % k != 0:
        return False
    target = s // k
    used = [False] * n
    arr.sort(reverse=True)
    def search(groups):
        if all(val == target for val in groups):
            return True
        if any(val > target for val in groups):
            return False
        for i in range(n):
            if not used[i]:
                used[i] = True
                if search([groups[j] + arr[i] for j in range(k)]):
                    return True
                used[i] = False
                if groups.count(0) > 0:
                    break
        return False
    return search([0]*k)
