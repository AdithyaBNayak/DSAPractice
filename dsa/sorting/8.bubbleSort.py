"""
Swap if the next element is smaller than the present element
"""


# Function Definition
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

# driver Code
arr =  [1,56,38,95,8,47,97,63]
result = bubbleSort(arr)
print(" The sorted array is as follows")
print(result)