# Find Square root of number using Binary Search

# Function Definition
def find_sqrt(n):
    start = 0
    end = n

    while start <= end:
        mid = start + (end-start)//2
        
        if mid * mid == n:
            return mid
        
        elif mid * mid > n:
            end = mid - 1

        else:
            ans = mid
            start = mid + 1
    return ans           


# Driver Code
print("Enter the number: ")
n= int(input())

print(f"Square Root: {find_sqrt(n)}")