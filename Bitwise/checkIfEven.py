"""
Check if the given number is Even using bitwise operator
"""
# Definition
def isEven(n):
    if n & 1 == 0:
        return True
    return False    


# Driver
print("Enter the number to be checked: ")
n = int(input())
if isEven(n):
    print("Number is even")
else:
    print("Number is odd(not even)")    