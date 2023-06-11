# Function Defintion
def reverseInt(n):
    ans = 0
    while n > 0:
        rem = n % 10
        ans = ans*10 + rem
        n = n//10
    return ans    




# Driver Code
print("Enter an Integer: ")
n = int(input())
reversedValue = reverseInt(n)
print(f"The Reveresed Value is : {reversedValue}")
