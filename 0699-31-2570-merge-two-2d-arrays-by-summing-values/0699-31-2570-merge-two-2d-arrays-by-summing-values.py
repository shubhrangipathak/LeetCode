class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i,j in nums1:
            d[i] = d.get(i, 0) + j
    
        for i,j in nums2:
            d[i] = d.get(i, 0) + j
    
        print (d)
        return sorted([[i, j] for i, j in d.items()] )


      
        