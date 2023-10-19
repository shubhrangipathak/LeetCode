class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return n
        
        idx = 1
        
        for i in range(2, n):
            if nums[i] != nums[idx - 1]:
                
                idx += 1
                
                nums[idx] = nums[i]
                
        return idx + 1
                
