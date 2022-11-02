class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        max_heap=[]
        for char,freq in d.items():
            heappush(max_heap,(-freq,char))
        res=[]
        r=""
        while max_heap:
            p=heappop(max_heap)
            for i in range(-p[0]):
                r+=p[1]
                
        return r
