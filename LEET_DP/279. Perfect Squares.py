import math
class Solution:
    def numSquares(self, n: int) -> int:
        
        ## 划分性
        ## f[i] = min {f[i-j^2] + 1, f[i]}
        ## f[i] i 表示为i = 几个平方的和
        
        f= [None]*(n+1)
        f[0] = 0
        for i in range(1,n+1):
            f[i] = math.inf
            for j in range(1,int(math.sqrt(n)+1)):
                if (j*j)<=i:
                    f[i] = min(f[i],f[i-j*j]+1)
                    ## 有多少种方式： min 改为求和
                    ## 能不能表示成K个平方的和：
                    ## f[i][k] = OR {f[i-j^2][k-1]}
        print(f)
        return f[n]
        
        
        
        
        