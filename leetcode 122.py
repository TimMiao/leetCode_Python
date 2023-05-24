import math
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                the_profit = prices[i + 1] - prices[i]
                profit += the_profit
        return profit