class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        res = 0
        
        for i in range(26):
            alpha = chr(97 + i)
            
            if alpha in word and alpha.upper() in word:
                 res += 1
                    
        return res