class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        v = set(nums)
        i = 1
        while 1:
            if i not in v:
                return i
            i += 1
            
#METHOD 2
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        
        for i in nums:
            d[i] = d.get(i,0)+1
        #Accessing values from a dictionary takes O(1) time.
        
        val = 1
        
        while 1:
            
            if val not in d:
                return val
            
            val += 1
