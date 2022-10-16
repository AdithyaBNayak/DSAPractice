""" 
Given a sorted array
Apply ternary search 

"""
# Function Definition
def ternarySearch(arr, key, l, r):
    mid1 = l + (r-l)//3
    mid2 = r - (r-l)//3
    while l <= r:
        if arr[mid1] == key :
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif key < arr[mid1]:
            return ternarySearch(arr,key,l,mid1-1)
        elif key > arr[mid2]:
            return ternarySearch(arr,key,mid2+1,r)        
        else:
            return ternarySearch(arr,key,mid1+1, mid2-1)
    return -1        
     

# Driver Code
arr = [20,25,47,56,59,63,65,79,82]
key = 59
index = ternarySearch(arr, key, 0, len(arr)-1)
print("The index of the key is ", index)