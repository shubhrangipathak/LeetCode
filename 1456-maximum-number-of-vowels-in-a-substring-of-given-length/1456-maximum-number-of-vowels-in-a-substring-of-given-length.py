class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        d = "aeiou"
        
        i = 0
        j = 0 
        count = 0
        mx = 0
        while j < n:
            if j-i+1 <= k:
                if s[j] in d:
                    count += 1
                j += 1
            else:
                if s[i] in d:
                    count -= 1
                i += 1
            mx = max(mx,count)
            
        return mx
       