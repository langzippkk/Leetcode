class Solution:
    def maxKilledEnemies(self, A: List[List[str]]) -> int:
        
        
        
        if(A == None or len(A) == 0 or len(A[0]) == 0):
            return 0
        
        m = len(A)
        n = len(A[0])
        
        up = [[0 for x in range(n)]  for x in range(m)]
        down = [[0 for x in range(n)]  for x in range(m)]
        left = [[0 for x in range(n)]  for x in range(m)]
        right = [[0 for x in range(n)]  for x in range(m)]
        
        for i in range(m):
            for j in range(n):
                up[i][j] = 0
                if (A[i][j]!= 'W'):
                    if A[i][j]== 'E':
                        up[i][j]+=1
                        
                    if (i > 0):
                        up[i][j] += up[i-1][j]
                        
        for i in range(m):
            for j in range(n):
                left[i][j] = 0
                if (A[i][j]!= 'W'):
                    if A[i][j]== 'E':
                        left[i][j]+=1
                        
                    if (j > 0):
                        left[i][j] += left[i][j-1]
                
        for i in range(m):
            for j in reversed(range(n)):
                right[i][j] = 0
                if (A[i][j]!= 'W'):
                    if A[i][j]== 'E':
                        right[i][j]+=1
                        
                    if (j <  n-1):
                        right[i][j] += right[i][j+1]         
                        
        for i in reversed(range(m)):
            for j in range(n):
                down[i][j] = 0
                if (A[i][j]!= 'W'):
                    if A[i][j]== 'E':
                        down[i][j]+=1
                        
                    if (i < m-1):
                        down[i][j] += down[i+1][j]
                        
                    
        res = 0    
        for i in range(m):
            for j in range(n):
                if (A[i][j]!= 'W'):
                    if A[i][j]== '0':
                        res = max(res,up[i][j]+right[i][j]+left[i][j]+down[i][j])
                        
        return res
                        
                        
                        
                        
                        
                        
                        
                        
                
        