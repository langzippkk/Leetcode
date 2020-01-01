import math
class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        
        ## function: f[i][j] = min{f[i-1][j] , f[i][j-1]} + A[i][J]
        
        ## initial condition: f[0][0] = A[0][0]
        
        ## boundary condition: no need
        if (A == None or len(A) == 0 or len(A[0]) == 0):
            return 0
        m = len(A)
        n = len(A[0])
        f = [[None for x in range(n)] for x in range(m)]
        
        pi =  [[None for x in range(n)] for x in range(m)]
        
        for i in range(m):
            for j in range(n):
                f[i][j] = math.inf
                if i == j ==0:
                    f[i][j] =A[i][j]
                    continue
                if (i>0):
                    f[i][j] = min(f[i-1][j]+A[i][j],f[i][j])
                    
                if (j>0):
                    f[i][j] = min(f[i][j-1]+A[i][j],f[i][j])
        print(f)
        ## print path from m-1,n-1
        
        return f[m-1][n-1]