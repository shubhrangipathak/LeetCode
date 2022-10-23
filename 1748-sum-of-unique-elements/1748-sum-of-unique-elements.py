class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        s=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums:
            if d[i]==1:
                s+=i
        return s