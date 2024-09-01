class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m * n:
            return []
        
        res = []
        
        for i in range(m):
            
            row = []
            
            for j in range(n):
                
                idx = i * n + j
                
                row.append(original[idx])
                
            res.append(row)
        
        return res