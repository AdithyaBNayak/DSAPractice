"""
Create a numeric Palindrome Equilateral Pyramid
    1
   212
  32123
 4321234
543212345
"""
def printPattern(n):
    for i in range(1,n+1):
        l = 1
        for j in range(1,n+i):
            if j <= n-i:
                print(' ', end="")
            elif j <= n:
                print(l, end= '')
                l += 1
            else:
                print(l-2,end='')
                l -= 1                    
        print()        

# Driver code
print("Enter the number of rows:")
n = int(input())
printPattern(n)