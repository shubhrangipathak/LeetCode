class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        def is_prime(n):
            if n <= 1:
                return False
            elif n <= 3:
                return True
            elif n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        res = []
        for i in range(len(nums)):
            if is_prime(nums[i]):
                res.append(i)
                
        return abs(res[0] - res[-1]) if len(res) > 1 else 0
    