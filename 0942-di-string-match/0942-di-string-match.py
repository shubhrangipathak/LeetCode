class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n=len(s)
        i=0
        j=n
        res=[]
        for char in s:
            if char=='I':
                res.append(i)
                i+=1
            else:
                res.append(j)
                j-=1

        res.append(i)
        
        return res
                