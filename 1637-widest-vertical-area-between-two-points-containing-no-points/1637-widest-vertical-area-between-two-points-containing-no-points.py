class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = []
        for x,y in points:
            l.append(x)
            
        l.sort()
        res = 0 
        for i in range(len(l)-1):
            res = max(res,l[i+1]-l[i])
            
        return res
