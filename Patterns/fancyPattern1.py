"""

********1********
*******2*2*******
******3***3******
****4******4*****
***5********5****

"""


def printPattern(n):
    if n > 9:
        print("Please add value lesser than n")
        return
    
    for i in range(0,n):
        start_num_index = 8 - i 
        num = i # value to be printed will be the rowth value 
        count_num = 0 #  to make sure each num n is printed n times
        for j in range(0,17):
            if start_num_index == j and count_num <= num :
                    print(num+1,end='')
                    start_num_index += 2
                    count_num += 1
            else:
                print("*",end='')          
            
        print()        

# Driver code
print("Enter the number of rows:")
n = int(input())
printPattern(n)