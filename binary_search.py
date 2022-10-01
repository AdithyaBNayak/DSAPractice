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

arr = [ 2, 34, 5, 7, 46, 9, 77, 6, 9, 98, 67, 38 ]    
key = 46
index = binary_serach(arr , key , 0 , len(arr)-1 ) 
print(index)

    