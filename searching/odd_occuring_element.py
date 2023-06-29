# Find odd occurring element in an array 
"""
All numbers occur even number of times except one
All repeating occurence of elements occur in pairs
Pairs of same numbers are not adjacent
There cannot be more than 2 consequtive same elements
[1,1,2,2,3,3,4,4,3,600,600,4,4]
"""

"""
Solution: make XOR for all elements..We get the solution --->TC - O(n)

Solution2: Using Binary Search COncept
           Ans should always be in even index.


"""
def solve(arr):
    s = 0
    e  = len(arr) - 1
    while s <= e:
        mid = s + (e-s)//2
        if s == e:
            return s,arr[s]
        # Mid is even
        elif mid % 2 == 0:
            #  when even index and its next  elements are same go further right
            if mid+1< len(arr) and arr[mid] == arr[mid+1]:
                s = mid + 2
            # ELse 2 possibbilities
            # May be the mid is the answer, or can be left to it
            else:
                e = mid
        # Mid is odd
        else:
            # If the odd index element is same to its previous element
            # move right
            if mid-1 >= 0 and arr[mid] == arr[mid-1]:
                s = mid + 1
            else:
                e = mid - 1    




arr = [1,1,2,2,3,3,4,4,3,3,600,600,4,4,5]
index,value = solve(arr)
print(f"Index is  {index}")
print(f"Value is  {value}")
