class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = defaultdict(int)

        repeated = missing = -1 
        n = len(grid)

        size = n * n 

        for row in grid:
            for ele in row:
                d[ele] += 1 
        
        for i in range(1, size + 1):
            if d[i] == 2:
                repeated = i 
            if d[i] == 0:
                missing = i 

        return [repeated, missing]


        