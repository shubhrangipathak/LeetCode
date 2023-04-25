class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        v = set(nums)
        i = 1
        while 1:
            if i not in v:
                return i
            i += 1