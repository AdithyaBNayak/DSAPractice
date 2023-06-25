"""
Common elements in 3 sorted array
Expected TC - O(n1+n2+n3)
Expected SC - O(n1+n2+n3)
"""

# Function Definition
def find_common_ele(arr1,arr2,arr3):
    i=j=k = 0
    output = set() #we choose set to avaoid duplicates
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    while i<n1 and j<n2 and k<n3:
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            output.add(arr1[i]) # instaed of append we use add
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return list(output)
    #If you donot want to use set() you can first remove duplicates from all 3 array and follow same steps           

# Driver Code
array1 = [1,5,10,20,40,80]
array2 = [6,7,20,80,100]
array3 = [3,4,15,20,30,70,80,120]
print("Common elements are: ")
print(find_common_ele(array1, array2, array3))

array5 = [3,3,3]
array6 = [3,3,3]
array7 = [3,3,3]
print("Common elements are: ")
print(find_common_ele(array5, array6, array7))