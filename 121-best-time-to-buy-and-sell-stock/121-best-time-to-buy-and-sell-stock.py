class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        minprice = prices[0]
        for i in range(1,len(prices)):
            if(prices[i]<minprice):
                minprice=prices[i]
            else:
                res = max(res,prices[i]-minprice)
        return res