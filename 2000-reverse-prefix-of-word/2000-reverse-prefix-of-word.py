class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        res = ""
        for i in range(len(word)):
            if word[i] == ch:
                s = word[:i + 1]
                s = s[::-1]
                res = s + word[i + 1:]
                
                return res