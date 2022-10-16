# Funtion Definition
def insertionSort(arr):
    n = len(arr) 
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while j>=0 and arr[j] > key:            
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
    
# Driver Code
arr = [2,89,94,734,64,76,46,84,47]
result = insertionSort(arr)
print(f"The sorted array  is :{result}")