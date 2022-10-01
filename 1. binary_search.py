def binary_serach(arr, key , l, r):

    while l <= r:

        mid = l + (r-l)//2

        if arr[mid] == key :
            return mid

        elif arr[mid] > key : 
            return binary_serach(arr,key, l, mid-1)

        else:
            return binary_serach(arr,key, mid+1, r)        

    return -1

arr = [ 1,3,4,7,9,44,67,79,89 ]    
key = 89
index = binary_serach(arr , key , 0 , len(arr)-1 ) 
print(index)

    
