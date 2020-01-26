def matchingpairs(A,B):
    m = len(A)
    n = len(B)
    matchA = []
    matchB = []
    table = [[0 for i in range(n)]for j in range(m)]
    ## dp table
    flag = False
## for the record of A[0] or B[0] has been used for matching or not for initialization step.
    for i in range(m):
        for j in range(n):
            ## initialization t[0][0]
            if (A[i] == B[j] and i ==0 and j == 0):
                table[i][j] =3
                flag = True
            if (A[i] != B[j] and i ==0 and j == 0):
                table[i][j] = -3
            ## initialization t[0][j]
            if (A[i] == B[j] and i==0 and j>0 and flag == False):
                table[i][j] = table[i][j-1]+3+(3-2)
            if ((i==0 and j>0) and (A[i] != B[j] or A[i] == B[j] and flag == True)):
                table[i][j] = table[i][j-1]-2
            ## initialization t[i][0]
            if (A[i] == B[j] and i>0 and j == 0 and flag == False):
                table[i][j] = table[i-1][j]+3+(3-2)
            if ((i>0 and j==0) and (A[i] != B[j] or A[i] == B[j] and flag == True)):
                table[i][j] = table[i-1][j]-2
            ## recurrence
            if (A[i]==B[j] and i>0 and j>0):
                table[i][j] = max(table[i-1][j-1]+3,table[i-1][j]-2,table[i][j-1]-2)
            if(i>0 and j>0 and A[i] != B[j] ):
                table[i][j] = max(table[i-1][j-1]-3,table[i-1][j]-2,table[i][j-1]-2)

    return table

print(matchingpairs([0,1,2],[1,1]))




