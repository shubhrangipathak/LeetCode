class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for i in num:
            curr = i
            
            while k > 0 and stack and stack[-1] > curr:
                stack.pop()
                k -= 1 
                
            stack.append(curr)
            
        while k > 0:
            stack.pop()
            k -= 1 
        
        res = ''.join(stack).lstrip('0')
        
        if res:
            return res
        
        return "0"
        
       