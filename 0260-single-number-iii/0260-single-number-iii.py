class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
         
        n = len(nums)
        
        if n == 2:
            return nums
        
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1 
            else:
                d[i] = 1 
               
        nums.clear()
        for i,j in d.items():
            if j == 1:
                nums.append(i)
                
        return nums
            
            