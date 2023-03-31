class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row,col,grid):
            
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != '1':
                return 
            
            grid[row][col]='2'
            
            for direction in directions:
                new_r = row + direction[0]
                new_c = col + direction[1]
                dfs(new_r,new_c,grid)
        
        
        #Driver code for dfs function
        c = 0
        m = len(grid)  #Number of rows
        n = len(grid[0]) #Number of columns
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j,grid)
                    c += 1
        return c
        