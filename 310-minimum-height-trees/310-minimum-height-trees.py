class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            res = []
            for i in range(n):
                res.append(i)
            return res
        
        adj = [set() for _ in range(n)]
        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        
        leaves = []
        # adding all leaves into q
        for i in range(n):
            if(len(adj[i])==1):
                leaves.append(i)
        
        remain_nodes = n
        while(remain_nodes>2):
            remain_nodes = remain_nodes - len(leaves)
            new_leaves = []
            
            while leaves:
                l = leaves.pop()
                neigh = adj[l].pop()
                adj[neigh].remove(l)
                if(len(adj[neigh])==1):
                    new_leaves.append(neigh)
            leaves = new_leaves
        
        return leaves
                    
                