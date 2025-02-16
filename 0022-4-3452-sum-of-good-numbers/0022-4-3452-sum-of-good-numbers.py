class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tot = 0

        for i in range(n):
            flag = True
            if i - k >= 0 and nums[i] <= nums[i - k]:
                flag = False
            if i + k < n and nums[i] <= nums[i + k]:
                flag = False 
            
            if flag:
                tot += nums[i]

        return tot
