class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        mod = 10 ** 9 + 7
        
        sub_arr = []
        
        for i in range(n):
            s = 0
            for j in range(i,n):
                
                s += nums[j]
                sub_arr.append(s)
                
        sub_arr.sort()
        
        return sum(sub_arr[left - 1:right]) % mod