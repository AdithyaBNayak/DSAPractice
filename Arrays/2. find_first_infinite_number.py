''' 
Find the first occurence of infinite number in a list of unsorted numbers having all the infinite numbers at the end of the list

'''


# We use modified binary search approach 

def find_first_inf(arr, l, r):
    mid = l+ (r-l)//2

    # In case the is no inifinite number
    if arr[mid] != float('inf') and mid == r:
        return -1
    # In case there is no infinite number until middle index 
    elif arr[mid] != float('inf') :
        return find_first_inf(arr, mid+1, r)

    # In case when we find infinite for arr[mid], but also find its previous number to be same 
    elif mid !=0 and arr[mid-1] == float('inf'):
        return find_first_inf(arr, l, mid-1 )   

    # In case we find the index     
    else:
        return mid    


arr = [5,7,2,7,4, float('inf'),float('inf'),float('inf'),float('inf')]
print(find_first_inf(arr,0,len(arr)-1))


