"""
 Given a string s, return "TRUE"
 if the s can be palindrome after deleting at most one character from it

Example1: aba -> True
Example2: abca -> True 
"""
def palindrome(s,i,j):
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True    


def  check(s):
    l = 0
    r = len(s) - 1

    while l <= r:
        print(f"l = {l} and r = {r}")
        if s[l] != s[r]:
            return palindrome(s,l+1,r) or palindrome(s,l,r-1) 
        
        l += 1
        r -= 1

    return True

str1 = "aba"
str2 = "abbca"
str3 = "acbcca"
str4 = "eeccccbebaeeabebccceea"
str5 = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(check(str5))

