def recover_permutation(n, k, a):
    res = [-1] * n
    for i in range(n):
        if res[i] == -1:
            res[i] = a[i]
            j = (i + k) % n
            while j != i:
                if res[j] != -1 and res[j] != a[i]:
                    return [-1]
                res[j] = a[i]
                j = (j + k) % n
    return res

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = recover_permutation(n, k, a)
    if ans[0] == -1:
        print(-1)
    else:
        print(*ans)
