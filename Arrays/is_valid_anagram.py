class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i],0) + 1 
            t_dict[t[i]] = t_dict.get(t[i],0) + 1           

        if len(s_dict) != len(t_dict):
            return False

        for character in s_dict:
            if s_dict[character] != t_dict.get(character,0):
                return False
        
        return True
