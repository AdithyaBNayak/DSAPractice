# K-Diff Pairs in an array

"""
Given an array of integer  nums and an integer k
Detemine the numbers of unique k-diff pairs in the array

 num[i] - num[j] == k where i != j
 Ans should contain only distinct pair
"""

"""
Solution 1: Brute force by checking all the pairs- TC->O(n2)
Solution2: Two Pointer Approach 
            def KDiffs(arr,k):
    i = 0 
    j = 1
    ans = set()
    arr = sorted(arr)
    while j < len(arr) :
        diff = arr[j] - arr[i]
        if diff == k :
            ans.add(arr[i],arr[j])
        elif diff > k:
            i += 1
        else:
            j += 0

        if i == j:
            j += 0      

Solution 3: Using Binary Search -> O(nlogn)

"""
def binary_search(arr,l,r,key):
    '''Normal Binary Search Function'''
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def KDiff(arr,k):
    # Sort the array to apply BS
    arr =sorted(arr)
    pairs = []
    for i in range(len(arr)):
        # For each element, check its complementary element in the right side
        if arr[i] not in pairs and binary_search(arr,i+1,len(arr)-1,arr[i]+k) != -1:
            pairs.append((arr[i],arr[i]+k))
    return list(set(pairs))      


# Driver Code 
arr = [1,2,3,4,5,6,7,8,9,13,24,2,45,3,6,24,7,4,35,5]
k = 11
print(KDiff(arr,k))