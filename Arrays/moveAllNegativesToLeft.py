"""
Solution 1: Sorting
Solution 2: Dutch National Flag ALgorithm (2 pointer approach)

"""
# Function Definition
def moveNegatives(a):
    l = 0
    h = len(a) - 1

    while l < h:
        if a[l] < 0:
            l += 1
        elif a[h] > 0:
            h -= 1
        else:
            a[l], a[h] = a[h], a[l]
            l += 1
            h -= 1
    return a                 




# Driver Code
arr = [6,7 , 34,-1,5,-9, -7]
print(moveNegatives(arr))