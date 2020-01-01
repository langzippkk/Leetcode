class Solution:
    def longestCommonSubsequence(self, AA: str, BB: str) -> int:
        ## github also use this
        # 找对子（对应的字母）
        # 1. A[m-1] not in 对子 + subproblem：A[0...m-1] and 
        # B[0---n-2]
        # 2 B[n-1] not in 对子 + subproblem: A[0---m-2] and B[0....n-1]
        # 3. there is pair of A[m-1] -> B[m-1] here A[m-1] = B[m-1] and subproblem: A[0....m-2] and B[0...n-2]
        
        # initialization: f[i][j]: A[0..i-1] and B[0...j-1] common subsequence
        
        # f[0][j] = 0
        # f[i][0] = 0
        
        ## recursion： f[i][j] = max{f[i-1][j],f[i][j-1],f[i-1][j-1]+1 |given A[i-1] = B[j-1]}
        
        m = len(AA)
        n = len(BB)
        f = [[0 for x in range(n+1)] for x in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if (i==0 or j == 0):
                    f[i][j] = 0
                    continue
                f[i][j] = max(f[i][j-1],f[i-1][j])
                if (AA[i-1] == BB[j-1]):
                    f[i][j] = max(f[i][j],f[i-1][j-1]+1)
        return f[m][n]
                    
        
                
        
        
        
        
        
        
        
        