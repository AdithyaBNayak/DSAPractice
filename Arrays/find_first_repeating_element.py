# Find First Repeating ELement
'''
Question:
If none of the elements are repeating return -1
[1,5,4,3,5,6] ---> Solution is 5
'''


# Function Definition
def firstRepeatingElement(arr):
    # Solution 1
    # Brute Force Approach with TC - O(n2)

    # Solution 2 - Using dictionaries (Here TC->O(n) and SC -> O(n))
    occurence = {}
    for element in arr:
        if element in occurence:
            occurence[element] += 1
            if  occurence[element] == 2:
                return element
        else:
            occurence[element] = 1
    return -1        


# Driver Code
array = [1,5,4,3,5,6]
print(f"First Repeating element of the dictionary isL : {firstRepeatingElement(array)} ")
array2 = [1,2,3,4]
print(f"First Repeating element of the dictionary isL : {firstRepeatingElement(array2)} ")
