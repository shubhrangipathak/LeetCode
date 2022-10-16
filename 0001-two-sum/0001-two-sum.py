class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d1=nums[i]
            d2=target-d1
            if d1 in d:
                return [i,d[d1]]
            else:
                d[d2]=i