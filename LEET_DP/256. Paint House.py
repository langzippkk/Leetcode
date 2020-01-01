import math
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        ## we need to know min cost of first N-1 th house and 
        ## N-1 is blue,green or red
        #seq type
        n = len(costs)
        f = [[0 for x in range(3)] for x in range(n+1)]
        f[0][0] = f[0][1] = f[0][2] = 0
        for i in range(1,n+1):
            for j in range(3):
                f[i][j] = math.inf
                for k in range(3):
                    if j == k:
                        continue
                    f[i][j] = min(f[i][j],f[i-1][k]+costs[i-1][j])

        print(f)
                    
        return min(f[n][0], f[n][1],f[n][2])