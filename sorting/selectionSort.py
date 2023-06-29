"""
Selecting the smallest value's index in each pass
Keeping the small elements from left to right



Time COmplexity
i = 0 j = 1,2,3,4
i = 1 , j = 2,3,4
i = 2,  j = 3,4
i = 3,  j = 4
n = n *(n+1)//2--------> O(n2)
"""


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr           

arr = [1,21,7,67,4,6,2,65,34,75,23]
print(selection_sort(arr))