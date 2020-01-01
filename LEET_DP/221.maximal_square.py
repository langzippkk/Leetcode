class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        
        ## 1. 确定状态：L1: (i-1,j-1)
        ##  L2: (i-1,j)
        ## L3: (i,j-1)
        ## f[i][j] 以i，j 为右下角的边长
        ## 如果 (i,j) 格 是 1， = min{f[i-1][j],f[i][j-1],f[i-1][j-1]}+1 
        ## 木桶原理
        
        if(A == None or len(A) ==0 or len(A[0])==0):
            return 0
        res = 0
        m = len(A)
        n = len(A[0])
        f = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                if (A[i][j] == '0'):
                    f[i][j] = 0
                    continue
                    
                    
                f[i][j] = 1
                if(i>=1 and j >= 1):
                    f[i][j] = min(min(f[i-1][j],f[i][j-1]),f[i-1][j-1])+1
                
                res = max((f[i][j]*f[i][j]),res)
                
        return res