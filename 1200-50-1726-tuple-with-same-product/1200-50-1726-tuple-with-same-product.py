class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        n = len(nums)
        res = 0 

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                res += 8 * freq[prod]
                freq[prod] += 1 
        
        return res