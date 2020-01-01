import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1 = math.inf
        ## 时刻保持一个最低价格，0 to j-1 called pi
        ## find 最大的 pj - pi, which is profit here
        profit = 0
        for i in range(len(prices)):
            if prices[i]<min1:
                min1 = prices[i]
            if profit < (prices[i] - min1):
                profit = prices[i] - min1
                
        return profit
            
            