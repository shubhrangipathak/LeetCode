class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        
        count = 0
        
        s = sorted(intervals , key = lambda val : (val[0] , -val[1]))
        
        end = s[0][1]
        
        for i in range(1,n):
            if s[i][1] <= end:
                count += 1 
                
            else:
                end = s[i][1]
                
        return n - count
        
        
        