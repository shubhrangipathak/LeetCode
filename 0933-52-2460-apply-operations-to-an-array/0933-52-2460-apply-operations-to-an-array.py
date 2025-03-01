class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2 
                nums[i + 1] = 0
        
        non_zeros = [i for i in nums if i != 0]
        count_zeros = len(nums) - len(non_zeros)

        return non_zeros + [0] * count_zeros
