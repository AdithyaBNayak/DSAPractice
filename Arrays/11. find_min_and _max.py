"""
Find minima and maxima using Divide and Conquer approach
"""

# Function Definition
def findMaxAndMin(arr, i, j):
    ## Small Problem 
    if i == j:
        minEle = arr[i]
        maxEle = arr[i]
    elif i == j - 1:
        if arr[i] < arr[j]:
            minEle = arr[i]
            maxEle = arr[j]
        else:
            minEle = arr[j]    
            maxEle = arr[i]
    # Big Problem 
    # Divide and Conquer Approach
    else:
        # Divide 
        mid = i + (j-i)//2 
        # Conquer 
        max1, min1 = findMaxAndMin(arr, i, mid)
        max2, min2 = findMaxAndMin(arr,mid+1,j)
        # Combine 
        minEle =  min1 if min1 < min2 else min2
        maxEle = max1 if max1> max2 else max2

    return maxEle, minEle

# Driver Code
arr = [75, 45, 95, 50, 60, 67, 29, 32]
max, min =  findMaxAndMin(arr,0, len(arr)-1)
print(f" The miximum and minimum values in the given array are {max} and {min} respectively")
