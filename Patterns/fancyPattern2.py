"""
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1
 For n=4
"""


def printPattern(n):
    # Growing Phase
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end="")
            num+=1
            if j < i:
                print("*",end='')          
        print()

    start = num
    # Shrinking Phase
    for i in range(n):
        start = start - (n-i)
        num = start
        for j in range(0,n-i):
            print(num, end="")
            num += 1
            if j < n-i-1:
                 print("*",end='')      
        print()        
       

# Driver code
print("Enter the number of rows:")
n = int(input())
printPattern(n)