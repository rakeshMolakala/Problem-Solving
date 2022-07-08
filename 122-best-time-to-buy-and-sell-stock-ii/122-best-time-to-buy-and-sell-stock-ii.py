class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def recur(i,buy):
            
            if(i==len(prices)-1):
                if(buy):
                    return 0
                else:
                    return prices[i]
                
            if((i,buy) in cache):
                return cache[(i,buy)]
            
            res = 0
            ## Allowed to buy
            if(buy):
                # buy
                p1 = -prices[i] + recur(i+1,False)
                # not buy
                p2 = recur(i+1,True)
                res = max(p1,p2)
            ## Allowed to sell
            else:
                # sell
                p1 = prices[i] + recur(i+1,True)
                # not sell
                p2 = recur(i+1,False)
                res = max(p1,p2)
                
            cache[(i,buy)] = res
            return res
               
        cache = dict()
        return recur(0,True) 