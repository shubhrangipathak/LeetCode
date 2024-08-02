class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        
        nums = nums + nums 
        
        n = len(nums)
        
        x = 0
        ones_in_window = 0 
        
        for i in range(n):
            if i >= ones and nums[i - ones]:
                x -= 1 
                
            if nums[i] == 1:
                x += 1 
            
            ones_in_window = max(ones_in_window, x)
            
        return ones - ones_in_window
            
   