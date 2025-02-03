class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1

        inc = 0 
        dec = 0 

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if inc == 0:
                    inc = 2 
                else:
                    inc += 1 
                res = max(res, inc)
                dec = 0
            
            elif nums[i] < nums[i - 1]:
                if dec == 0:
                    dec = 2 
                else:
                    dec += 1 
                res = max(res, dec)
                inc = 0
            
            else:
                inc = 0 
                dec = 0 
        return res
