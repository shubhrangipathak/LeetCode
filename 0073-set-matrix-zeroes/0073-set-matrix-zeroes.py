class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row = [0] * m
        col = [0] * n
        
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j] == 0:
                    
                    row[i] = "a"
                    col[j] = "a"
                    
        for i in range(m):
            for j in range(n):
                if row[i] == "a" or col[j] == "a":
                    matrix[i][j] = 0