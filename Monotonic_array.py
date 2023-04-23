def isMonotonic(array):
    increasing = True
    decreasing = True
    
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            decreasing = False
        elif array[i] < array[i-1]:
            increasing = False
    
    return increasing or decreasing
