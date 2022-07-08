class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Top Down
        n = len(prices)
        def recur(i,buy,number):
            # Base cases
            if(number==k):
                return 0
            if(i==n-1):
                if(buy):
                    return 0
                else:
                    return prices[i]
            
            
            # using Cached result
            if((i,buy,number) in cache):
                return cache[(i,buy,number)]
            
            res = 0
            if(buy):
                # will buy
                p1 = -prices[i] + recur(i+1,False,number)
                # not buy
                p2 = recur(i+1,True,number)
                res = max(p1,p2)
            else:
                # will sell
                p1 = prices[i] + recur(i+1,True,number+1)
                # not sell
                p2 = recur(i+1,False,number)
                res = max(p1,p2)
            
            cache[(i,buy,number)] = res
            return res
        
        cache = dict()
        if(len(prices)==0):
            return 0
        return recur(0,True,0)        