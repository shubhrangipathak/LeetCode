class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n+1)]for j in range(m+1)]
        
        max_Area = 0
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    max_Area = max(max_Area,dp[i][j])
                    
        return max_Area * max_Area