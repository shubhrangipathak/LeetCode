class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n
        nums.sort()
        
        while i < j and i+2 < j:
            if nums[i] == nums[i+2]:
                i+=3
                
            else:
                break
            
        return nums[i]
                