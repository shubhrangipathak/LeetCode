class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        i = 0
        res = [""]*numRows      
        for letter in s:
            if i == numRows-1:  
                mov_down = False
            elif i == 0:        
                mov_down = True 
            res[i] += letter 
            if mov_down:
                i+=1 
            else:
                i-=1   								
        return "".join(res)