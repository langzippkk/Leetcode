class Solution:
    def numDecodings(self, s: str) -> int:
        ## look at the last number
        ## recursive: (N-3) + last two or (N-2) + last one
        
        # f[i] = f[i-1 | last one match a digit] + f[i-2 | last two digit match a digit]
        
        ## initial condition: f[0] = 1
        n = len(s)
        f = [None]*(n+1)
        if n ==0:
            return 0
        f[0] = 1
        for i in range(1,n+1):
            f[i] = 0
            if s[i-1] != '0':
                f[i]+=f[i-1]
                
            ##last two
            if i>=2 and ((s[i-2] == '1') or (s[i-2] == '2' and s[i-1] <= '6')):
                f[i] += f[i-2]
        print(f)
        return f[n]
            
        
        