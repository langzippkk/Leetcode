class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    ## 如果B 最后一位是*：
    ##  1.如果 A[m-1] 不被 * 匹配，* 代表空： 能否匹配取决于 A【0.。。m-1】
    ## 和 B【0.。。n-2】
    ## eg：A：ABC   B: ABC*
    ## 要看 A[0...m-1] 和 B[0...N-2] 是否匹配
    ## Here f[i][j] = f[i][j-1]
    
    ## 2. 如果 A[m-1] 被 * 匹配
    ## eg：A：ABCDEFS   B: ABC*
    ## Here f[i][j] = f[i-1][j]   
    ## 要看 A[0...m-2] 和 B[0...N-1] 是否匹配
    ## ！！继续用B的*匹配A剩下的字符，所以B不动
    
    ## 3.如果 最后一位不是*
    ## when i>0 : B[j-1] = '?' or A[i-1] = B[j-1]
    ##    f[i][j] = f[i-1][j-1]
    
    ## initialization
    ## f[0][0] =True
    ## f[1][0] = ....f[m][0] = False, when j = 0
    ## when i = 0, need to calculate use recursive function
    
    
        m = len(s)
        n = len(p)
        f = [[None for x in range(n+1)] for x in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if(i==0 and j==0):
                    f[i][j] = True
                    continue
                if(j == 0):
                    f[i][j] = False
                    continue
                f[i][j] = False

                ## 1. 如果B 最后一位不是*：
                if (p[j-1] != '*'):
                    ## !!!! i > 0
                    if(i>0 and (p[j-1] == '?' or p[j-1] == s[i-1])):
                        f[i][j] = f[i-1][j-1]

                else:
                    ## 1. 如果*match nothing： here we also considering the case
                    ## that i = 0 and j>0: eg: A: empty B: **
                    f[i][j] = f[i][j-1]
                    ## 2. A 去掉尾巴，继续匹配前面

                    ## ! only consider this when i>0 because: 
                    ## i-1 might be < 0 !
                    if (i>0):
                        f[i][j] = f[i][j] or f[i-1][j]

        return f[m][n]
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    