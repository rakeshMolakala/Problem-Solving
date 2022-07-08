class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        def recur(i,buy):
            if(i==n-1):
                if(buy):
                    return 0
                else:
                    return prices[i]-fee
            
            if((i,buy) in cache):
                return cache[(i,buy)]
            
            res = 0
            if(buy):
                p1 = -prices[i] + recur(i+1,False)
                p2 = recur(i+1,True)
                res = max(p1,p2)
            else:
                p1 = prices[i] - fee + recur(i+1,True)
                p2 = recur(i+1,False)
                res = max(p1,p2)
            
            cache[(i,buy)] = res
            return res
             
        cache = dict()
        return recur(0,True)