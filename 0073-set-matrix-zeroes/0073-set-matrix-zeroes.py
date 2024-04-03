class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def row_zero(i):
            for col in range(n):
                if matrix[i][col] != 0:
                    matrix[i][col] = "a"
                    
        
        def col_zero(j):
            for row in range(m):
                if matrix[row][j] != 0:
                    matrix[row][j] = "a"
                    
        
        #Main function
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n): 
                
                if matrix[i][j] == 0: 
                    row_zero(i)
                    col_zero(j)
                        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0