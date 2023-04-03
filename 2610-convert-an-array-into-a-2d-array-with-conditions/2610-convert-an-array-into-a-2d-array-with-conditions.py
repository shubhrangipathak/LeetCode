class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        
        res = [] 
        for i in nums:
            if i in d:
                d[i]+=1
        
            depth = d[i]
            
            if len(res) <= depth:
                res.append([])
                
            res[depth].append(i)
            
        return res