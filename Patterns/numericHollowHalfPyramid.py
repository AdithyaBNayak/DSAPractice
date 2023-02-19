"""
Create a numeric hollow half pyramid

1
12
1 3
1  4
12345
"""
def printPattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            # Print all numbers for last column
            # print only 1st and last number 
            if i ==n or j == 1 or j == i:
                print(j,end= '')                
            # Add the spaces in between    
            else:
                print(" ", end='')
        print()        

# Driver code
print("Enter the number of rows:")
n = int(input())
printPattern(n)