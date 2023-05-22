class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if x == y:
                continue
            elif x != y:
                stones.append(abs(y-x))
            
        if len(stones):
            return stones[0]
        return 0
                

