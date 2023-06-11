# Function Definition
def isPrime(num):
    for j in range(2, num//2+1):
        if num % j == 0:
            return False
    return True        

def primeNumberTillN(n):
    i = 2
    while i <= n:
        if isPrime(i):
            print(i, end=" ") 
        i += 1       


# Driver Code:
print(" Enter the Number N: ")
n = int(input())
primeNumberTillN(n)
 