class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        list1 = [None for i in range(n)]
        matrix = []
        for i in range(m):
            matrix.append(list1)
            
        for i in range(m):
            for j in range(n):
                if(i == 0 or j == 0):
         ## the initial condition 
                    matrix[i][j] =1 
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                    
        return matrix[m-1][n-1]