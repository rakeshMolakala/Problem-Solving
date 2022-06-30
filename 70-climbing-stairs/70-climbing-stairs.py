class Solution:
        
    def climbStairs(self, n: int) -> int:
        cache = dict()
        return self.recur(n,cache)
        
        
    def recur(self,n,cache):
        if(n in cache):
            return cache[n]
        if(n==0):
            return 1
        if(n==1):
            return 1
        cache[n] = self.recur(n-1,cache)+self.recur(n-2,cache)
        return cache[n]
    
        
        
        
        