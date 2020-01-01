class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        
        m = len(A)
        n = len(A[0])
        print(m,n)
        if (A == None or m == 0 or n == 0):
            return 0
        res = [[0 for x in range(n)] for x in range(m)]
        ## this create m by n matrix
        for i in range(m):
            for j in range(n):
                if (A[i][j] == 1):
                    ## obstacle
                    res[i][j] = 0
                    continue
                if ((i == 0) and (j == 0)):
                    res[i][j] = 1
                    continue
                print(i,j)
                res[i][j] = 0
                ## begin populate
                if (i>0):
                    res[i][j] += res[i-1][j]
                if (j>0):
                    res[i][j] += res[i][j-1]

        return res[m-1][n-1]