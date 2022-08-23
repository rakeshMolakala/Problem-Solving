class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        n = len(prices)
        for i in range(1,n):
            if(prices[i]>min_price):
                profit = max(profit, prices[i] - min_price)
            else:
                min_price = prices[i]
        return profit