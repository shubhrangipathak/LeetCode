class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         def solve(row,col,matrix):
#             if col<0 or col>=len(matrix):
#                 return 10001
#             if row == len(matrix)-1:
#                 return matrix[row][col]
#             ans1 = matrix[row][col]+solve(row+1,col-1,matrix)
#             ans2 = matrix[row][col]+solve(row+1,col,matrix)
#             ans3 = matrix[row][col]+solve(row+1,col+1,matrix)
#             return min(ans1,ans2,ans3)
        
#         minPath = float('inf')
#         for col in range(len(matrix)):
#             pathSum = solve(0,col,matrix)
#             minPath = min(minPath,pathSum)
            
#         return minPath


        def solve(row,col,matrix,dp):
            
            if col < 0 or col >= n:
                return 10001
            
            if row == n-1:
                return matrix[row][col]
            
            if dp[row][col] != -1:
                return dp[row][col]
            
            ans1 = matrix[row][col] + solve(row+1,col-1,matrix,dp)
            ans2 = matrix[row][col] + solve(row+1,col,matrix,dp)
            ans3 = matrix[row][col] + solve(row+1,col+1,matrix,dp)
            
            dp[row][col] = min(ans1,ans2,ans3)
            
            return dp[row][col]
        
        min_PathSum = float('inf')
        n = len(matrix)
        dp = [[-1 for i in range(n)]for i in range(n)]
        
        for col in range(n):
            PathSum = solve(0,col,matrix,dp)
            min_PathSum = min(min_PathSum,PathSum)
            
        return min_PathSum