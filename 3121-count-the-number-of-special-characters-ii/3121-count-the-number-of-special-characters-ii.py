class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        
        s = set()
        
        j = 0
        
        for i in word:
            if i.islower():
                if i.upper() not in s:
                    if i not in word[j + 1:] and i.upper() in word[j + 1:] and i.upper() not in word[:j]:
                        s.add(i)
                        s.add(i.upper())
                        res += 1 
                        
            j += 1
                        
                    
        return res