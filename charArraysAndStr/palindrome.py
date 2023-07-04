# Find if the given string is a palindrome

def palindrome(text):
    i = 0
    j = len(text) - 1

    while i <= j:
        # The below check ignores the casing
        if text[i] != text[j] and abs(ord(text[i]) - ord(text[j])) != 32:
            return False
        i += 1
        j -= 1

    return True

# Driver Code
print(palindrome("AdiThyaYhtidA"))

# print(chr(65))