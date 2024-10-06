class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        binaries = [bin(num)[2:] for num in nums]

        def concat_binaries(a,b,c):
            return int(a + b + c, 2)

        return max(concat_binaries(a, b, c) for a, b, c in permutations(binaries))