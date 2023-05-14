class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        
        left = 0
        right = n - 1
        
        top = 0
        bottom = n - 1
        
        val = 1
        
        while top <= bottom and left <= right:
            #Traverse top row.
            for col in range(left,right+1):
                res[top][col] = val
                val += 1
            
            top += 1
            
            #Traverse right column.
            for row in range(top,bottom+1):
                res[row][right] = val
                val += 1
                
            right -= 1
            
            if top <= bottom:
                for col in range(right,left-1,-1):
                    res[bottom][col] = val
                    val += 1
                    
                bottom -= 1 
                
            if left <= right:
                for row in range(bottom,top-1,-1):
                    res[row][left] = val 
                    val += 1
                    
                left += 1
                
        return res
        