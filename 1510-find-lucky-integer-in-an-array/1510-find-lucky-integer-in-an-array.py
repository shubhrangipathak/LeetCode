class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}

        for i in arr:
            d[i] = d.get(i, 0) + 1

        res = []
        maxi = -1
        for i, j in d.items():
            if i == j:
                if i > maxi:
                    maxi = i

        return maxi