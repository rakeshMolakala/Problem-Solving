class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for road in roads:
            g[road[0]].append(road[1])
            g[road[1]].append(road[0])
        
        maxi = 0
        for i in range(n):
            for j in range(i+1,n):
                if j in g[i]:
                    maxi = max(maxi,len(g[i])+len(g[j])-1)
                else:
                    maxi = max(maxi,len(g[i])+len(g[j]))
        
        return maxi
                
        