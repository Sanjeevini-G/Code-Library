class Solution:
    # Function to sort the stack such that the top element is max
    # s is a stack
    def sorted(self, s):
        # Reverse the stack to get it in ascending order
        s.reverse()
        
        # Use the given code snippet to sort the stack in descending order
        temp_stack = []
        while s:
            temp = s.pop()
            while temp_stack and temp_stack[-1] > temp:
                s.append(temp_stack.pop())
            temp_stack.append(temp)
        while temp_stack:
            s.append(temp_stack.pop())
        
        # Reverse the stack again to get it in descending order
        s.reverse()



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends
