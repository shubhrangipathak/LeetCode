class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        
        left = 0 
        right = n - 1
        res = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if letters[mid] > target:
                res = mid 
                right = mid - 1 
                
            else:
                left = mid + 1
            
        return letters[res]