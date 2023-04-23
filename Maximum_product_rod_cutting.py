def max_product_cut(n):
    if n == 2 or n == 3:
        return n-1
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    product *= n
    return product

n = int(input("Enter the length of the rod: "))
max_product = max_product_cut(n)
print("Maximum product:", max_product)
