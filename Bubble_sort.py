def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = list(map(int, input("Enter the array elements: ").split()))
bubble_sort(arr)
print("The sorted array is:", arr)
