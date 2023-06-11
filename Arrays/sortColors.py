"""
Red = 0 
Orange = 1
Blue = 2

Sort suych that all red comes first, and then orange and then blue

Must solve thiswithout sorting function
"""

"""
Counting method- get count of each color and create array

Inplace, 3 pointer approach

"""
# Function Definition
def sortColors(a):
    l = 0
    m = 0
    h = len(a) - 1

    while m <= h:
        if a[m] == 0:
            a[m],a[l] = a[l],a[m]
            l += 1
            m += 1
        elif a[m] == 1:
            m += 1
        else:
            a[m], a[h] = a[h], a[m]
            h -= 1

    return a               

# Driver Function
arr = [1,0,2,2,1,1,0,0,0,2,1]
print("Sorted array is :")
print(sortColors(arr))