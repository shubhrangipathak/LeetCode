class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #Method 1
        
#             target.sort()
#             arr.sort()

#             return target == arr

        #Method 2 
    
        d = {}
        d2 = {}
        
        for i in target:
            d[i] = d.get(i,0) + 1 
            
        
        for i in arr:
            d2[i] = d2.get(i,0) + 1 
            
        return d == d2
            
  