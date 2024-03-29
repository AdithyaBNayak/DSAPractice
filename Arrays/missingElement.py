"""
Find missing number from array with Duplicates

Array of size N and elemnts are in range (1,N)

Example:
Array of size 5
[1,3,5,4,3]
Ans: 2

"""

# Function Definition
def missingElement(arr):
    # Solution 1: Visiting an element and considering its value to be index for next. 
    # Marking visited element as negative
    for  i in range(len(arr)):
        index = abs(arr[i]) # Note : abs() is necessary
        if arr[index-1] > 0:
            arr[index-1] *= -1
    # Printing index of positive number
    for j in range(len(arr)):
        if arr[j] > 0:            
            return j+1 

    # Solution2: Sorting+ Swapping Method
    



# Driver Code
arr = [1,2,5,3,6,7,2,8,4]
print(f"Missing Element is {missingElement(arr)}")