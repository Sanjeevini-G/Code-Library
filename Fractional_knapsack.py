class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        # Calculate the value-to-weight ratio for each item and store it in a list.
        ratios = [(item.value/item.weight, item.value, item.weight) for item in arr]
        # Sort the items in descending order of their value-to-weight ratio.
        ratios.sort(reverse=True)
        # Initialize variables to keep track of total value and remaining weight.
        total_value = 0
        remaining_weight = W
        # Loop through the sorted items and add them to the knapsack as long as there is space.
        for ratio, value, weight in ratios:
            if remaining_weight == 0:
                break
            elif weight <= remaining_weight:
                total_value += value
                remaining_weight -= weight
            else:
                total_value += ratio * remaining_weight
                remaining_weight = 0
        # Return the maximum total value.
        return total_value

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends
