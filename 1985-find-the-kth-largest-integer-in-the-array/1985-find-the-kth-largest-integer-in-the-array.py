class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap=[]
        for i in nums:
            heappush(heap,-(int(i)))
        l=[]
        while k>0:
            x=heappop(heap)
            l.append(-1*x)
            k-=1
        return str(l[k-1])
