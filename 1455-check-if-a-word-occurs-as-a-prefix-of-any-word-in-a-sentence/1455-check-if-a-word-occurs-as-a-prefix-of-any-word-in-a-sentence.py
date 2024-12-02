class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        d = {}
        l = sentence.split(" ")
        m = len(searchWord)
        
        for i in range(len(l)):
            d[i+1] = l[i]
            
        for i,j in d.items():
            if len(j) >= len(searchWord):
                if j[:m] == searchWord:
                    return i
        return -1
            
       