# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for round in range(1,n):
        # Round should start from 1 to end of the array
        val = arr[round]
        j = round - 1

        while j>=0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1

        # Below for loop also can be provided instead             

        # insert the value in appropiate place    
        arr[j+1] = val

        '''
        for j in range(round - 1, -2, -1):
            # j should move from round -1 till -1(Note: not till 0)

            # Check for all previous elements
            if j>=0 and arr[j] > val:
                # If the previous value is greater, then copy the value to next place
                # j>0 condition is provided to avoid cases when j = -1
                arr[j+1] = arr[j]
            else:
                # As we mover right, the left part keeps getting sorted.
                break
        ''' 
        
    return arr

# Driver Code
arr = [7,87,7,56,3,5,24,63,13,53,23]
print(insertion_sort(arr))

