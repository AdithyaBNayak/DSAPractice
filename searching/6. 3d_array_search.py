'''
Each row in sorted order
last element of each row is smaller than first element of the next row
Find row_no and column_no of the element

'''
# In such case we can convert 3D array to 2D array
# row_no = mid //n
# column_no = mid % n

def search(arr,key,l,r):    
    while l <= r:
        mid = l + (r-l)//2
        mid_elem = arr[mid//n][mid%n]
        if key == mid_elem:
            return mid//n,mid%n
        elif key < mid_elem:
            r = mid - 1
        else:
            l = mid + 1        
    return -1,-1

arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
key = 6
m = len(arr)
n = len(arr[0])
print(search(arr,key,0,m*n-1))        