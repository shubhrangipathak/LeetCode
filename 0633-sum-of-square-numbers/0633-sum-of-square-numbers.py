class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d={}
        for i in range(0,int(c**0.5)+1):
            a=i*i
            b=c-a 
            if a not in d:
                d[a]=i
            if b in d:
                    return True
        return False