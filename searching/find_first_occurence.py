# FInd first occurence of an element in a sorted array
def find_first_occurence(arr,l,r,key):
    mid = l + (r-l)//2
    ans = -1
    while l <= r:
        mid = l + (r-l)//2
        # Store ans andmove left
        if key == arr[mid]:
            ans = mid
            r = mid -1
        elif key > arr[mid]:
            l = mid+1
        else:
            r = mid -1

    return ans

arr = [1,2,3,4,4,7,8,9,9]
print(find_first_occurence(arr,0,len(arr)-1,4))