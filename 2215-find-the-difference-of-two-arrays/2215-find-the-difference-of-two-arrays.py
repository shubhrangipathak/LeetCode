class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n =2
        res = []
        for i in range(2):
            res.append([])
        for i in nums1:
            if i not in nums2:
                res[0].append(i)
                
        for i in nums2:
            if i not in nums1:
                res[1].append(i)
        res[0] = list(set(res[0]))
        res[1] = list(set(res[1]))
        return res