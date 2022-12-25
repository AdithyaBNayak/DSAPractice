# Function definition
def findPower(a,n):
    # Small Problem
    if n == 1:
        return a
    elif n == 0 :
        return 1
    # Big Problem
    else:
        # Divide
        mid = n//2
        # Conquer
        b = findPower(a,mid)
        # Combine
        result = b * b
    if n % 2 == 0:
        return result
    return result * a     

# Driver Code
a = 2
n = 5
power = findPower(a,n)
print(f"{a} to the power {n} is {power} ")                 
