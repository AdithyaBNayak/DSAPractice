# Bubble Sort

"""
For every ith round, we will keep ith largest element in its place
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(1,n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]

        if swapped == False:
            # If not swapped, it is already sorted
            break        
    return arr

arr = [1,21,7,67,4,6,2,65,34,75,23]
print(bubble_sort(arr))