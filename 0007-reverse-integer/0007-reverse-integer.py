class Solution:
    def reverse(self, x: int) -> int:
        
        if x>0:
            s=1 
        else:
            s=-1 
        num=int(str(abs(x))[::-1])
        res=s*num 
        if -2**31<=res<=2**31-1:
            return res
        return 0
        

