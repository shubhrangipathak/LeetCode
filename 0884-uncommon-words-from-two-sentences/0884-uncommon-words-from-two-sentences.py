class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1 = s1.split(" ")
        lst2 = s2.split(" ")
        
        d1 = {}
        d2 = {}

        for i in lst1:
            d1[i] = d1.get(i,0) + 1 
        
        for i in lst2:
            d2[i] = d2.get(i,0) + 1 
        
        res = []
        for i,j in d1.items():
            if j == 1 and i not in d2:
                res.append(i)
        
        for i,j in d2.items():
            if j == 1 and i not in d1:
                res.append(i)

        return res
        
       