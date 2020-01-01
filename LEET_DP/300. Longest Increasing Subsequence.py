class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## 状态： f[j]: 以a[j]结尾的max increasing subsequence
        ## so we will need max() function
        ## f[j] = max{1,f[i]+1}, here j>i,a[j]>a[i]
        
        
        if (nums == 'None' or len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return 1
        n = len(nums)
        f = [1] *n
        ## least possible is 1
        for i in range(n):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    f[j] = max(f[i]+1,f[j])
        return max(f)
        
        
        