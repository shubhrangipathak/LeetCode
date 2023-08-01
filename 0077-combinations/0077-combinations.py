class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        stack = [(1,[])]
        
        res = []
        
        while stack:
            
            num, curr_comb = stack.pop()
            
            if len(curr_comb) == k:
                res.append(curr_comb)
                
            else:
                for i in range(num,n+1):
                    stack.append((i+1,curr_comb+[i]))
                
                
                
        return res
            
            
                    
            
        