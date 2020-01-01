class Solution:
    def countBits(self, n: int) -> List[int]:
        ## remove the rightest digit, /2, write as i >>1
        ## remove the leftest digit, *2 
        
        ## f[i] = f[i removed the rightest] + (i mod 2)
        
        
        f= [0]*(n+1)
        f[0] = 0
        for i in range(n+1):
            f[i] = f[i>>1] + (i%2)
            
        return f
            