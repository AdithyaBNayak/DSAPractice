"""
Finding power of an element using divide and conquer Approach
"""
# Function Definition
from unittest import result


def powerOfEle(ele,n):
    # Small Problem 
    if n == 0:
        return 1
    elif n == 1:
        return ele 
    # Big Problem 
    else:
        # Divide 
        mid = n//2
        # Conquer
        b = powerOfEle(ele,mid)
        # Combine 
        result = b* b
    # When the power element is of odd case we need to multiply the result by element        
    return result if n % 2 == 0 else result*ele


# Driver code 
element = 2
power = 6
solution =  powerOfEle(element,power)
print(f"{element} to the power {power} is {solution}") 
