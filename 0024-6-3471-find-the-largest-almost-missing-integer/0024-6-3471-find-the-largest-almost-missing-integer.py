class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)
        
        c = Counter(nums)
        print(c)
        if k == 1:
            return max((i for i in c if c[i] == 1), default = -1)
        
        res = -1 
        if c[nums[0]] == 1:
            res = nums[0]
        if c[nums[-1]] == 1: 
            res = max(res, nums[-1])
        return res

        