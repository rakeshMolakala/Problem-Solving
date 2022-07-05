class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        def recur(i,target):
            if(target==0):
                return 1
            if(i==0):
                if(target%coins[i]==0):
                    return 1
                else:
                    return 0
            if((i,target) in cache):
                return cache[(i,target)]
            notTake = recur(i-1,target)
            take = 0
            if(target>=coins[i]):
                take = recur(i,target-coins[i])
            res = take + notTake
            cache[(i,target)] = res
            return res
        
        cache = dict()
        return recur(len(coins)-1,amount)
                
        
        