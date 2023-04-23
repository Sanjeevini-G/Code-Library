def find_missing_numbers(arr):
    max_val = max(arr)
    nums = set(arr)
    all_nums = set(range(1, max_val + 1))
    missing_nums = all_nums - nums
    return sorted(list(missing_nums))

arr = list(map(int, input("Enter the integer array separated by space: ").split()))
missing_nums = find_missing_numbers(arr)
print(missing_nums)
