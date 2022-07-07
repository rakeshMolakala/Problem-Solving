class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        
        for i in range(1,len(prices)):
            curr_profit = prices[i]-min_price
            profit = max(profit,curr_profit)
            min_price = min(min_price,prices[i])
        return profit