class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                res=abs(d[nums[i]]-i)
                if res<=k:
                    return True
            d[nums[i]]=i
        return False                
        