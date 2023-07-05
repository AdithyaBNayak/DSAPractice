# Remove all Adjacent Duplicates in a String
"""
Example Input: abbaca
Output ca
"""

def remove_adj_duplicates(s):
    i = 0
    ans = ""

    while i < len(s):
        print(f"Ans:{ans}")
        if len(ans) > 0  and ans[len(ans)-1] == s[i]:
            ans = ans[0:len(ans)-1]
        else:
            ans = ans + s[i]
        i += 1    

    return ans

# Driver Code
s = "abbaca"
# s = "addhaakkakkdood"
print(remove_adj_duplicates(s))