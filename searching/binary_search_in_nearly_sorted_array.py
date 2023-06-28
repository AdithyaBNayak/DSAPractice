# Binary Search in the nearly sorted array

"""
[10,3,40,20,50,80,70]
Nearly sorted array - any element which has to be in ith position
But is actually in (i+1)th or (i-1)th position

"""
#Function Defintion
def search(arr,target):
    l = 0
    h = len(arr) - 1

    while l <= h:
        mid = l + (h-l)//2

        if arr[mid] == target:
            return mid
        elif mid+1 < len(arr) and arr[mid+1] == target:
            return mid+1
        elif mid-1 >0 and  arr[mid-1] == target:
            return mid-1
        elif target < arr[mid]:
            h = mid - 2
        else:
            l = mid + 2

    return -1            

# Driver Code
arr = [10,3,40,20,50,80,70]
print("Enter a target value")
key = int(input())

print(search(arr,key))

arr2 = [10, 7]
print(search(arr,key))
