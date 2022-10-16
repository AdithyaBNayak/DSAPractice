"""
Selecting the smallest value's index in each pass
"""

# Function Definition
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]        
    return arr

# Driver Code 
arr = [3,65,84,48,57,95,67,7,99,489,43,56]
result =  selectionSort(arr)
print(f" The sorted array is : {result} ")