class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_heap=[]
        res=[]
        s=[i*i for i in nums]
        for i in s:
            heappush(min_heap,i)
        while min_heap:
            res.append(heappop(min_heap))
        return res
            