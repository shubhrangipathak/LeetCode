class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res = []
        
        for candy in candies:
            new_candy = candy + extraCandies
            m = max(candies)
            if new_candy >= m:
                res.append(True)
            else:
                res.append(False)
                
        return res
        