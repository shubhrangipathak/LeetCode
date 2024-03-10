class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        res = []
        
        for i in nums1:
            d[i] = d.get(i , 0) + 1
            
        for i in nums2:
            if i in d:
                res.append(i)
                del d[i]
                
        return res