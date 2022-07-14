class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        def recur(i,j):
            if(i==j-1 ):
                return 0
            if((i,j) in cache):
                return cache[(i,j)]
            res = math.inf
            if(cuts[0]>=j):
                return 0
            for x in cuts:
                if(x>i and x<j):
                    cost = j-i + recur(i,x) + recur(x,j)
                    res = min(res,cost)
            if(res==math.inf):
                res = 0
            cache[(i,j)] = res
            return res
                    
        cuts.sort()
        cache = dict()
        return recur(0,n)