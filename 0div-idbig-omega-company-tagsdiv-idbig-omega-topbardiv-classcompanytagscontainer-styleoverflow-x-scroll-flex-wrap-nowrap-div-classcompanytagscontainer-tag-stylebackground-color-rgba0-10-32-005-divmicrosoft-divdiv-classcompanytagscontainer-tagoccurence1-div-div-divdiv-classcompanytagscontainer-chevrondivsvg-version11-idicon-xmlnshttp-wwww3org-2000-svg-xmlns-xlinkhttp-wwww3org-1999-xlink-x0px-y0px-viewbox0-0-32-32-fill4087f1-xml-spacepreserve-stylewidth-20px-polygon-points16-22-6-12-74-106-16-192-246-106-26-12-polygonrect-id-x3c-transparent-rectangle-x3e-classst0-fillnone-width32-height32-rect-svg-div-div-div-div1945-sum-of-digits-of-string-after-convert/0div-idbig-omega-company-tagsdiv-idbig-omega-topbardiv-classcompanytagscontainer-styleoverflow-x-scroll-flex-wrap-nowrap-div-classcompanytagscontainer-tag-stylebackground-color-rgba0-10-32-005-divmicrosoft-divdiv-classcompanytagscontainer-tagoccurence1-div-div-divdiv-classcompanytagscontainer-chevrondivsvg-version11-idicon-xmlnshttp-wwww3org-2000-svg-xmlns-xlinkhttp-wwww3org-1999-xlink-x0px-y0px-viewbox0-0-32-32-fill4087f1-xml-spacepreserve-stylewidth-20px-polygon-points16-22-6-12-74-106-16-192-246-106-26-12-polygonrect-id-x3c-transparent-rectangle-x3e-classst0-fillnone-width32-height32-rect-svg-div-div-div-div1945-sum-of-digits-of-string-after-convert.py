class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        num_s = ""
        
        for i in s:
            
            num_s += str(ord(i) - ord('a') + 1)
            
        while k > 0:
            
            res = 0
            
            for i in num_s:
                res += int(i)
            
            num_s = str(res)
        
            k -= 1
            
        return res