class Solution:
    def isInterleave(self, A: str, B: str, X: str) -> bool:
        
        ## 1. f[s][i][j] 前S个字符是否由A前i个字符和B前j个字符组成
        
        ## and s = i+j
        
        ## recursion: f[i][j] 前i+j 个字符是否由前i个字符和B前j个字符交错形成  = (f[i-1][j] AND x[i+j-1] = A[i-1])
        
        ## OR (f[i][j-1] AND X[i+j-1] == B[j-1])
        
        ## initialization : f[0][0] = 0
        
        ## boundary: i = 0 and j = 0
        
        m = len(A)
        n = len(B)
        
        if (len(X) != (m+n)):
            return False
        
        f = [[None for x in range(n+1)] for x in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                ## empty
                if (i==0 and j==0):
                    f[i][j] = True
                    continue
                
            # boundary condition
                
        ## 3 conditions:
            # i = 0
            # j = 0
            # i ,j > 0
                f[i][j] = False
                ## i-1 is the last letter of A, i+j-1 is the last letter of X
                if (i>0 and X[i+j-1] == A[i-1] and f[i-1][j]):
                    f[i][j]  = True
                if (j>0 and X[i+j-1] == B[j-1] and f[i][j-1]):
                    f[i][j]  = True
        return f[m][n]
                
                
                
                
                
                
                
                
                
                
        