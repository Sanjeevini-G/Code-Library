def trap(height):
    n = len(height)
    left, right = 0, n - 1
    maxLeft, maxRight = 0, 0
    ans = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                ans += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                ans += maxRight - height[right]
            right -= 1

    return ans

n = int(input("Enter the length of the height array: "))
height = list(map(int, input("Enter the height array: ").split()))

print("Amount of trapped rain water:", trap(height))
