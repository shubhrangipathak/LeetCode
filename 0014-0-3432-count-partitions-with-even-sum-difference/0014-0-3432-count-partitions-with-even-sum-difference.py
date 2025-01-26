class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        c = 0 

        leftsum = 0 

        for i in range(n - 1):
            leftsum += nums[i]
            rightsum = total_sum - leftsum

            if leftsum % 2 == rightsum % 2: 
                c += 1 
        return c 