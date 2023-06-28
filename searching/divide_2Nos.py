# Divide 2 numbers using Binary Search
"""
quotient*divisor <= dividend
so we keep the range from 0 to dividend

"""
# Function Definition
def divide(divisor,dividend):
    s = 0
    e = abs(dividend)
    ans = 0
    while s < e:
        mid = s +(e-s)//2
        if mid * abs(divisor) == abs(dividend):
            if (dividend < 0 and divisor > 0 ) or (dividend > 0 and divisor < 0):
                return mid * -1
            return mid
        elif mid * abs(divisor) < abs(dividend):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    if (dividend < 0 and divisor > 0 ) or (dividend > 0 and divisor < 0):
        return ans * -1        
    return ans            
        

# Driver Code

print(divide(2,13))