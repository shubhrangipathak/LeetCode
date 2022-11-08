class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        s=[list(i) for i in zip(efficiency,speed)]
        s.sort(reverse=True)
        min_heap=[]
        high_speed=0
        res=0
        for ef,sp in s:
            if len(min_heap)==k:
                high_speed-=heappop(min_heap)
            high_speed+=sp
            heappush(min_heap,sp)
            res=max(res,high_speed*ef)
            # print(min_heap)
        
        return res%(10**9+7)