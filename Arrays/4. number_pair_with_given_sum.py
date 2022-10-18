# Find the first pair of number in the given sorted list having the sum equal to the provided value 
# Its a sorted list 

# This solution follows 2 pointer approach
def find_pair(arr,l,r, sum_value):

    while l <= r:
        if arr[l] + arr[r] == sum_value:
            return l,r
        elif arr[l] + arr[r] > sum_value:
            r = r - 1
        else: 
            l = l + 1        
    return -1,-1

arr = [20, 40, 60, 80 , 90, 120, 240]
sum_val = 210
position = find_pair(arr,0, len(arr)-1, sum_val)
print(position)
