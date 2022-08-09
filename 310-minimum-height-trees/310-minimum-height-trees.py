class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            res = []
            for i in range(n):
                res.append(i)
            return res
        
        # creating adjacency list
        adj = [set() for _ in range(n)]
        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        
        # adding first set of leaves to leaves list
        leaves = []
        for i in range(n):
            if(len(adj[i])==1):
                leaves.append(i)
        
        # we'll keep on removing nodes that are leaves until we are down to 2 or 1 node
        remain_nodes = n
        while(remain_nodes>2):
            remain_nodes = remain_nodes - len(leaves)
            new_leaves = []
            
            while leaves:
                l = leaves.pop()
                # getting the only neighbor of the lead node
                neigh = adj[l].pop()
                # removing the connection 
                adj[neigh].remove(l)
                # adding to new_leaves list only if the neighbor is a leaf after removing connection with present leaf
                if(len(adj[neigh])==1):
                    new_leaves.append(neigh)
            leaves = new_leaves
        
        return leaves
                    
                