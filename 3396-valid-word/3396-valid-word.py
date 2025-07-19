class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        
        if n < 3:
            return False 

        dig = "0123456789"
        vow = "aeiouAEIOU"

        vowels = 0 
        consonants = 0

        for c in word:
            if c.isalpha():
                if c in vow:
                    vowels += 1
                else:
                    consonants += 1
            elif c not in dig:
                return False  

        return vowels >= 1 and consonants >= 1