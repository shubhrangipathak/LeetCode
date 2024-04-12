class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        high1 = 0
        high2 = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            if height[l] < height[r]:
                high1 = max(high1, height[l])
                total += high1 - height[l]
                l += 1
            
            else:
                high2 = max(high2, height[r])
                total += high2 - height[r]
                r -= 1
                
        return total
       
        