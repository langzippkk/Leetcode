class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        
        ## f[i][j][k][h] = True : T[k,h] can derived from S[i,j]
        
        ## dimension reduction: j-i = h-k
        
        ## then f[i][k][length] is enough,means s1 start with i can transfer to s2 start with k  with length "length" or not
        
        ## recursive: f[i][j][k] = OR{f[i][j][w] AND f[i+w][j+w][k-w]}   this is s1_1 = s2_1, s1_2 = s2_2
        ## OR {f[i][j+k-w][w] AND f[i+w][j][k-w]} k is the total length , w is the split point, this is s1_1= s2_2
        
        m = len(s1)
        n = len(s2)
        if (m!=n):
            return false
        f = [[[True for x in range(m+1)] for x in range (m)] for x in range (m)]

        # len = 1, initial condition
        for i in range(n):
            for j in range(m):
                f[i][j][1] = (s1[i] == s2[j])
                                
        for len1 in range(2,n+1):
            for i in range(n-len1+1):## s[i...i+len-1]
                for j in range(n-len1+1):## T[i...i+len-1]
                    
                    ## s1 has length w, s2 has length  len1-w
                    for w in range(1,len1):## the split point
                        
                        ## s1 has length w, s2 has length len-w
                        if (f[i][j][w] and f[i+w][j+w][len1-w]):
                            f[i][j][len1] = True
                            break
                        if (f[i][j+len1-w][w] and f[i+w][j][len1-w]):
                            f[i][j][len1] = True
                            break
        print(f)
        return f[0][0][n]
                            
                            
                        
        
        
        
        
        
        