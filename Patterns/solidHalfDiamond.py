"""
Solid Half Diamond

*
**
***
****
*****
****
***
**
*

"""


def printPattern(n):
    
    for i in range(1,2*n):
        if i <= n:
            for j in range(1,i+1):
                    print("*", end='')
        else:
            cond = n-(i%n) 
            for k in range(1,cond+1):
                print('*',end='')    
        
        print()        

# Driver code
print("Enter the number of rows:")
n = int(input())
printPattern(n)