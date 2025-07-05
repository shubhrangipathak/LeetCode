class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}

        for i in arr:
            d[i] = d.get(i, 0) + 1

        res = []
        for i, j in d.items():
            if i == j:
                res.append(i)

        if res:
            return max(res)
        return -1