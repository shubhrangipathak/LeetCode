class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mn_val=prices[0]
        ans=0
        if n<2:
            return 0
        for i in range(1,n):
            if prices[i]<mn_val:
                mn_val=prices[i]
            else:
                if prices[i]-mn_val>ans:
                    ans=prices[i]-mn_val
        return ans