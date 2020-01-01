class Solution:
    def findMaxForm(self, A: List[str], m: int, n: int) -> int:
        ## m个0，n个1， 最多能拼成list 里面的几个串
        
        
        ## 1.组成的最多的01串的子问题： 有没有最后一个字符串St-1
        
        ##1. 没有ST-1 ： 前T-1 个01串， 能组成几个01串
        
        ##2. 有ST-1： 假设 T-1 个01 串 有a(t-1) 个0 和 b(t-1) 个1      
         ##  需要知道前T-1 个01 串中， m-a(t-1), n-b(t-1) 能组成几个01串
            
        ## f[i][j][k] ： 前i个01串最多能有多少个被j个0 和 k个1组成
        ## = max{f[i-1][j][k], 1+f[i-1][j-a_(i-1)][k-b_(i-1)] given j>= a_(i-1) AND k>= b_(i-1)}
        
        
        if len(A) == 0:
            return 0
        ## count the 0 and 1 for each 01 string
        T = len(A)
        cnt0 = [0]*T
        cnt1 = [0]*T
        for i in range(T):
            s = str(A[i])
            for j in range(len(s)):
                if s[j]=='0':
                    cnt0[i]+=1
                else:
                    cnt1[i]+=1
        f = [[[0 for x in range(n+1)] for x in range(m+1)] for x in range(T+1)]
        
        ## consider i = 0, initialization
        
        for i in range(m+1):
            for j in range(n+1):
                
                f[0][i][j] = 0
                
        ## consider i > 0
        for i in range(1,T+1):
            for j in range(m+1):
                for k in range(n+1):
                    # cannot form the last one
                    f[i][j][k] = f[i-1][j][k]
                    
                    # can form the last one
                    
                    if (j>=cnt0[i-1] and k>=cnt1[i-1]):
                        ## enough to form the last one then:
                        
                        f[i][j][k] = max(f[i][j][k],f[i-1][j-cnt0[i-1]][k-cnt1[i-1]]+1)
                        
        ## answer is : max(f[T][0][0]....f[T][m][n])  
        
        res = 0
        for i in range(m+1):
            for j in range(n+1):
                res = max(res,f[T][i][j])

        return res
        
                    
            
        

        
        

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        
        
        
        
        
        