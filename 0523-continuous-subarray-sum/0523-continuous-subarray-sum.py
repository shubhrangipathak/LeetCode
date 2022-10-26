class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        d={0:-1}
        for i in range(1,n):
            nums[i]+=nums[i-1]
        print(nums)
        for i in range(n):
            nums[i]%=k
        print(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=i
        print(d)
        for i in range(n):
            if i-d[nums[i]]>1:
                return True
        return False
            
        
        
        
        
            
        
            