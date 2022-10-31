class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1=0
        p2=0
        n=len(nums)
        while p2<n:
            if nums[p2]==val:
                p2+=1
            else:
                if p1!=p2:
                    nums[p1],nums[p2]=nums[p2],nums[p1]
                p1+=1
                p2+=1
        return p1