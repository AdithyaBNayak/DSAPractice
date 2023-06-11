"""
Given a Number N and a value K from the right
Set the Kth Bit in Binary Representation of N.
The Position of Least Significant Bit (last bit) is zero, second last bit is 1 and so on

"""

"""
Solution:
 N = 10 
 K = 2

 N in binary = 1 0 1 0
 Place       = 3 2 1 0

 1 << K =  1 << 2 = 100
 N = 1 0 1 0
 K= 0 1 0 0 
 n | K =  1 1 1 0
"""
# Function Definition
def setKthBit(n,k):
    mask = 1 << k
    return n | mask





# Driver Code:
print("Enter an Number: ")
n = int(input())

print("Enter the value of K")
k = int(input())

print(f"Final Answer: {setKthBit(n,k)}")