def max_product_subset(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    negatives = [i for i in arr if i < 0]
    positives = [i for i in arr if i > 0]
    num_negatives = len(negatives)
    num_positives = len(positives)
    if num_negatives == n:
        return max(negatives)
    if num_negatives % 2 == 1:
        negatives.remove(max(negatives))
    if num_positives == 0 and num_negatives > 0:
        return 0
    product = 1
    for i in positives:
        product *= i
    for i in negatives:
        product *= i
    return product

arr = list(map(int, input("Enter the array: ").split()))
max_product = max_product_subset(arr)
print("Maximum product:", max_product)
