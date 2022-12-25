# Function definition
def findMinAndMax(arr,i,j):
    # Small Problem
    if i == j :
        min = arr[i]
        max = arr[i]
    elif j == i+1:
        if arr[i] < arr[j]:
            min = arr[i]
            max = arr[j]
        else:
            min = arr[j]
            max = arr[i]
    # Big Problem
    else:
        mid = i + (j-i)//2
        max1,min1 = findMinAndMax(arr,i,mid)
        max2,min2 = findMinAndMax(arr,mid+1,j)
        min = min1 if min1<min2 else min2
        max = max1 if max1>max2 else max2
    return max,min 

# Driver Code
arr = [3 ,3, 5,7, 9, 98, 78, 45, 23, 90, 1]
maxi , mini = findMinAndMax(arr, 0, len(arr)-1)
print(f"Maximum value= {maxi} and Minimum value= {mini}")
