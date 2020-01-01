class Solution:
    """
    @param k1: The coefficient of A
    @param k2: The  coefficient of B
    @param c: The volume of backpack
    @param n: The amount of A
    @param m: The amount of B
    @param a: The volume of A
    @param b: The volume of B
    @return: Return the max value you can get
    """
    def getMaxValue(self, k1, k2, T, n, m, a, b):
        # Write your code here
        
        ## key: 对于依次放入的两个同类物体，重量必须从小到大
        ## 所以可以对volumn从小到大排序：取A类的前i个 和B类的前J个
        
        ## 双序列形
        ## 情况：最后一个物品是A 还是B
        ## f[i][j] = max{f[i-1][j] + k(T-A0-...Ai-1-B0-...Bj-1),
        ## f[i][j-1]+k2(T-A0-B....Bj-1)}
        
        ## answer: max of f[i][j]
        f = [[0 for x in range(m+1)] for x in range(n+1)]
        a.sort()
        b.sort()

        asum = [0]*(n+1)
        bsum = [0]*(m+1)        
        asum[0] = 0 
        for i in range(1,n+1):
            asum[i] = asum[i-1]+a[i-1]
        bsum[0] = 0 
        for i in range(1,m+1):
            bsum[i] = bsum[i-1]+b[i-1]
        f[0][0] = 0 
        
        res = 0 
        
        for i in range(n+1):
            for j in range(m+1):
                ## first i A items,first j items
                if(i==0 and j==0):
                    continue
                tot = asum[i]+bsum[j]
                ## 总空间
                if (tot > T):
                    continue
                if (i>0):
                    f[i][j] = max(f[i][j],f[i-1][j]+k1*(T-tot))
                    
                if (j>0):
                    f[i][j] = max(f[i][j],f[i][j-1]+k2*(T-tot))
                    
                res = max(res,f[i][j])
                print(res)
        return res
