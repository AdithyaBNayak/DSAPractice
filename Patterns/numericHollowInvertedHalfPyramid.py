"""
Create a numeric hollow inverted half pyramid

12345
2  5
3 5
45
5
"""
def printPattern(n):
    for i in range(1,n+1):
        for j in range(i,n+1): 
            if i == 1 or j == i or j == n:
                print(j,end='')
            else:
                print(" ",end='')                           
        print()        

# Driver code
print("Enter the number of rows:")
n = int(input())
printPattern(n)