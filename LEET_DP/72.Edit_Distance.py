class Solution:
    def minDistance(self, A: str, B: str) -> int:
        ## NLP 生成句子， cost function
        
        ## 找顺序： 从前往后
        # 1. A插入A[n-1] -> B
        # 2. A replace 最后一个字符 -> B
        # 3. A 删除最后一个字符  
        # 4. A B最后一个本来就相等 A[0...N-2] 变成B[0...M-2]
        
        ## recursion：
        # f[i][j] A[0...i-1] to B[0...j-1] distance
        # f[m][n] ？
        # f[i][j] = min{f[i][j-1]+1,f[i-1][j]+1,f[i-1][j-1]+1,
        # f[i-1][j-1] given A[i-1] = B[j-1]}
        
        
        # initial : f[0][j] = j,f[i][0] = i
        m = len(A)
        n = len(B)
        
        f= [[0 for x in range(n+1)] for x in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    f[i][j] = j
                    continue
                    # insert
                if j == 0:
                    f[i][j] = i
                    continue
                    # delete
                
                f[i][j] = min(f[i][j-1]+1,f[i-1][j]+1,f[i-1][j-1]+1)
                if (A[i-1] == B[j-1]):
                    f[i][j] = min(f[i][j],f[i-1][j-1])
                    
        return f[m][n]
                    
                    
                    
        # f[i-1][j-1])
                
                    
        
                    
                    
                    
                    
                    
                    
        
        
        
        
        
        