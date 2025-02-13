class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1 
        mx = [0] * 82
        for i in nums:
            s = 0
            temp = i
            while temp != 0:
                s += temp % 10 
                temp //= 10 
            
            if mx[s] != 0:
                res = max(res, i + mx[s])
            
            mx[s] = max(mx[s], i)

        return res