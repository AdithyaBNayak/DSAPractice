# Add 2 numbers represented by arrays
"""
Example:
[1,2,3,4]
[4,5]
Solution= 1279
"""
arr1 = [9,9,9,9]
n1 = len(arr1)
arr2 = [9,9,9,9]
n2 =len(arr2)
carry = 0
ans= ""

while n1 !=0 and n2 != 0:
    summation = carry + arr1[n1-1] + arr2[n2-1]
    carry = summation//10
    digit = summation%10
    ans = str(digit) + ans
    n1 -= 1
    n2 -= 1

while n1 !=0 :
    summation = carry + arr1[n1-1] 
    carry = summation//10
    digit = summation%10
    ans = str(digit) + ans
    n1 -= 1

while n2 != 0:
    summation = carry + arr1[n1-1] + arr2[n2-1]
    carry = summation//10
    digit = summation%10
    ans = str(digit) + ans
    n2 -= 1    

if carry:
    ans = str(carry) + ans

print(int(ans))
