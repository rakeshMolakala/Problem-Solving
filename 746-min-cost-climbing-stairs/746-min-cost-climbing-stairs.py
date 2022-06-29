class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = dict()
        return min(self.recur(cost,0,cache),self.recur(cost,1,cache))
    
    
    def recur(self,cost,pos,cache):
        if(pos in cache):
            return cache[pos]
        if(pos>=len(cost)):
            return 0
        cache[pos] =  min(cost[pos]+self.recur(cost,pos+1,cache), cost[pos]+self.recur(cost,pos+2,cache))
        return cache[pos]
        