def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target element: "))
index = binary_search(arr, target)
if index != -1:
    print(f"The element {target} is found at index {index}")
else:
    print(f"The element {target} is not found in the array")
