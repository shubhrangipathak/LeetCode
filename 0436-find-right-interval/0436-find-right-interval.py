class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        def binary_search(val , s):
            start = 0 
            end = len(intervals) - 1 
            
            while start <= end:
                mid = (start + end) // 2
                
                if val <= intervals[mid][0]:
                    end = mid - 1 
                    
                else:
                    start = mid + 1 
                    
            return start
        
        
        
        d = {}
        
        #Dictionary to store the index of original intervals
        for i in range(len(intervals)):
            d[str(intervals[i])] = i
            
        intervals.sort()
        
        res = [-1] * len(intervals)
        
        for i in range(len(intervals)):
            pos = binary_search(intervals[i][1] , intervals)
            
            if pos < len(intervals):
                res[d[str(intervals[i])]] = d[str(intervals[pos])]
                
        return res
        
        
        
        
        
        