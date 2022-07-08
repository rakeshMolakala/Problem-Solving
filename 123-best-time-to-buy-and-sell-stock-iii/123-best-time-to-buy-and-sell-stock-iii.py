class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        def recur(i,buy,number):
            # Base cases
            if(i==n-1):
                if(buy):
                    return 0
                else:
                    return prices[i]
                
            if(number==2):
                return 0
            
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
        return recur(0,True,0)
            
            
        