class Solution:
    
    
    def minCut(self, s: str) -> int:
        ## f[i] = first i str can be partion to how many substring
        ## f[i] = min{f[j]+1 given s[j...i-1] is palin}
        ## palin[i][j]:i to j is palin or not.
        n = len(s)
        if (n == 0):
            return 0
        
        f= [0]*(n+1)
        palin = [[None for x in range(n)] for x in range(n)]
      ######## ispalin matrix  
        for i in range(n):
            for j in range(n):
                palin[i][j] = False
                
        for mid in range(n):
            # odd 
            i = j = mid
            while(i>=0 and j<n and s[i]==s[j]):
                palin[i][j] = True
                i = i-1
                j = j+1
             # even
            i = mid - 1
            j = mid
            while(i>=0 and j<n and s[i]==s[j]):
                palin[i][j] = True
                i = i-1
                j = j+1

        ##########################
                
        f[0] = 0
        for i in range(1,n+1):
            f[i] = math.inf
            for j in range(i):
                if (palin[j][i-1]):
                    f[i] = min(f[i],f[j]+1)

        #####    f[i] = min{f[j]+1 given s[j...i-1] is palin}
                    
                        
                    
        return f[n]-1