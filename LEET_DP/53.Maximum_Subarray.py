class Solution:
    def maxSubArray(self, S: List[int]) -> int:
        
        ## recurrence  max(s[i-1]+A[i],A[i])
        
        n = len(S)
        res = [None]*n
        for i in range(n):
            res[i] = 0
            if i ==0:
                res[i] = S[0]
            else:
                res[i] = max((S[i]+res[i-1]),S[i])
            
        return max(res)
        