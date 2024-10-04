class Solution:
    def minElement(self, nums: List[int]) -> int:
        def helper(n):
            sm = 0
            while n > 0:
                last_dig = n % 10
                sm += last_dig
                n //= 10
            return sm
        
        minv = float('inf')
        for i in nums:
            dig_sm = helper(i)
            if dig_sm < minv:
                minv = dig_sm 
                
        return minv