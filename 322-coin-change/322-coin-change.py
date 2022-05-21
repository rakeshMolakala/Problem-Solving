class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = dict()
        cache[0] = 0
        
        def recur(remain):
            if(remain<0):
                return math.inf
            if(remain==0):
                return 0
            if(remain in cache):
                return cache[remain]
            for x in coins:
                if(remain in cache):
                    cache[remain] = min(cache[remain],recur(remain-x)+1)
                else:
                    cache[remain] = recur(remain-x)+1
            return cache[remain]

        recur(amount)
        if(cache[amount]==math.inf):
            return -1
        return cache[amount] 
                
                
                