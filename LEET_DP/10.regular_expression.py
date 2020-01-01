class Solution:
    def isMatch(self, S: str, P: str) -> bool:
        m = len(S)
        n = len(P)
        
        # last digit of B is letter
        # A[m-1] = B[n-1] and A[0...m-2] match B[0..n-2]
        
        
        # is .
        # A[0...m-2] match B[0..n-2]
        
        
        # is *
        # condition 1: 0 个c A[0...m-1] match B[0...n-3]
        #f[i][j] = f[i][j-2]
        
        
        # condition 2: 多个c中的最后一个 and A[0...m-1] match B[0...n-2]
        # eg: A:ABCCC
        # B： ABC*
            # f[i][j] = f[i-1][j] if (B[j-2] = '.' OR B[j-2] == A[i-1] if B[j-1] = "*")
            
        ## initialization: f[0][0] = True
        
        
        f = [[None for x in range(n+1)] for x in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if (i==0 and j ==0):
                    f[i][j] = True
                    continue
                if (j==0):
                    # empty re cannot express anything
                    f[i][j] = False
                    continue
                    
                f[i][j] = False
                # last digit is not *
                if (P[j-1] != '*'):
                    if (i>0 and (P[j-1] == '.' or P[j-1] == S[i-1])):
                        f[i][j] = f[i-1][j-1]    
                else:
        # condition 1: 0 个c A[0...m-1] match B[0...n-3]
        #f[i][j] = f[i][j-2]
        # eg: A:ABCCC
        # B： ABC*D*
                    if (j>1):
                        f[i][j] = f[i][j-2]
        # condition 2: 多个c中的最后一个 and A[0...m-1] match B[0...n-2]
        # eg: A:ABCCC
        # B： ABC*
                    if (i>0 and j>1 and (P[j-2] == '.' or P[j-2] == S[i-1])):
                        f[i][j] = f[i][j] or f[i-1][j]
                        
        return f[m][n]
                
                         
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        