from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)==0:
            if(n<=1):
                return True
            return False
        
        g = defaultdict(list)
        for x in edges:
            g[x[0]].append(x[1])
            g[x[1]].append(x[0])
        visited = set()
        
        
        def dfs(node,prev):
            if node in visited:
                return False
            if(node not in visited):
                visited.add(node)
                for neigh in g[node]:
                    if(neigh!=prev):
                        if(not dfs(neigh,node)):
                            return False
            
            return True
                        
        return dfs(0,-1) and n==len(visited)
            
            
        
        
        
        
        