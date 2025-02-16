class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)

        j = 0 

        for i in range(n):
            if s[i] == s[j]:
                continue
            if i - j == k: 
                return True 
            
            j = i 
        return n - j == k