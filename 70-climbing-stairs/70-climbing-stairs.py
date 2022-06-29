class Solution:
    
    cache = dict()
    
    def climbStairs(self, n: int) -> int:
        cache = dict()
        return self.recur(0,n,cache)
        
        
    def recur(self,n,t,cache):
        if(n in cache):
            return cache[n]
        if(n==t):
            return 1
        if(n>t):
            return 0
        cache[n] = self.recur(n+1,t,cache)+self.recur(n+2,t,cache)
        return cache[n]
    
        
        
        
        