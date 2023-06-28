# Apply Binary Search on a 2D matrix

'''
m -> no. of columns
n -> no. of rows
total elements = m * n

For binary Search 
l = 0
r = m*n -1

rowIndex = mid // no.of columns
colIndex = mid % no. of columns
'''
def search(arr,target):
    m = len(arr[0])
    n = len(arr)

    l = 0
    r = m*n-1
    
    while l<=r:
        mid = l + (r-l)//2
        col = mid % m
        row = mid // m
        if arr[row][col] == target:
            return (row,col)
        elif arr[row][col] > target:            
            r = mid - 1
        else:
            l = mid + 1
    return (-1,-1)


# Driver Code
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
print("Enter a target value")
key = int(input())

print(search(arr,key))