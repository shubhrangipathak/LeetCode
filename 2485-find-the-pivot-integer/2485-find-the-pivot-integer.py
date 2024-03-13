class Solution:
    def pivotInteger(self, n: int) -> int:
        
        temp = (n * n + n) // 2 
        sq = int(sqrt(temp))
        
        if sq * sq == temp:
            return sq 
        
        return -1