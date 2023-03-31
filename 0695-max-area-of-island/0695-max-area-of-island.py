class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row,col,grid):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] != 1:
                return 0 
            grid[row][col] = "-1"
            c=1
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                c+=dfs(new_row,new_col,grid)
                
            return c
                
        
        
        m = len(grid)
        n = len(grid[0])
        maxc = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = dfs(i,j,grid)
                    maxc = max(maxc,cnt)
        return maxc