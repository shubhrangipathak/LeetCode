class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        
        res = []
        
        for i,j in c.items():
            if j > 1:
                res.append(i)
        
        return res