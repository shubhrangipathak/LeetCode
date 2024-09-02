class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        s = sum(chalk)
        # while k >= s:
        #     k -= s     //It's takes more time complexity
        
        k %= s
        
        for i in range(n):
            if chalk[i] > k:
                return i 
            k -= chalk[i] 