class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        c = 1
        
        res = [s[0]]
        
        for i in range(1, n):
            if s[i] == res[-1]:
                c += 1 
                if c < 3:
                    res.append(s[i])
                
            else:
                c = 1 
                res.append(s[i])
                
        return "".join(res)