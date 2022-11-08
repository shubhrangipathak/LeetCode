class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        currfuel=startFuel
        stops=0
        max_heap=[]
        for station in stations:
            pos,fuel=station[0],station[1]
            while currfuel<pos:
                if len(max_heap)==0:
                    return -1
                currfuel+=(-heappop(max_heap))
                stops+=1
            heappush(max_heap,-fuel)
        while currfuel<target:
            if len(max_heap)==0:
                return -1
            currfuel+=(-heappop(max_heap))
            stops+=1
        return stops