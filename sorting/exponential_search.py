# Exponential Search - finding the element in an infinite  array 
# This is used to search in a very long sorted array

def binary_search(arr,l,h,key):
    while l<=h:
        mid = l + (h-l)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            h = mid - 1
        else:
            l = mid + 1
    return -1

def exp_search(arr,key):
    if arr[0] == key:
        return 0

    i = 1
    n = len(arr)

    while i < n and arr[i] <= key:
        i *= 2

    return binary_search(arr, i//2, min(i,n-1),key)  

"""
Time Complexity - O(log(m)) where m is index of i(till where i reaches)
Binary Search (2^(log(m)) - 2^(log(m-1))) = 2 ^ (log(m-1))
Total = O(2^(log(m-1)))
"""            


# Driver Code
arr = [1,3,4,6,9,10,26,36,89,99,101]
print(exp_search(arr,89))