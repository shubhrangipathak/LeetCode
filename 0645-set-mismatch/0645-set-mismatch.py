class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        t,m=0,0
        for i in range(1,len(nums)+1):
            if d[i]==2:
                t=i
            if d[i]==0:
                m=i
        return [t,m]