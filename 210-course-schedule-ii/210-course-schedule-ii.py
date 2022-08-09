class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indegree = [0]*numCourses
        for e in prerequisites:
            adj[e[1]].append(e[0])
            indegree[e[0]]+=1
            
        # we'll use topological sort BFS fashion and first add the courses that have no dependency which means the courses having indegree as 0
        
        q = collections.deque()
        for i in range(numCourses):
            if(indegree[i]==0):
                q.append(i)
                
        if not q:
            return []
        
        coursesDone = []
        while(q):
            curr = q.popleft()
            coursesDone.append(curr)
            for neigh in adj[curr]:
                indegree[neigh]-=1
                if(indegree[neigh]==0):
                    q.append(neigh)
            
        if len(coursesDone)==numCourses:
            return coursesDone
        else:
            return []
        
        
#         pre = dict()
#         res=[]
#         if(len(prerequisites)==0):
#             for i in range(numCourses):
#                 res.append(i)
#             return res
        
#         for x in prerequisites:
#             if(x[0]==x[1]):
#                 return []
#             if(x[1] in pre):
#                 pre[x[1]].append(x[0])
#             else:
#                 pre[x[1]]=[x[0]]
                
#         vis=[0]*numCourses
#         dfsvis=[0]*numCourses
#         for i in range(numCourses):
#             newVis=[]
#             if(vis[i]==0):
#                 if(self.hasCycle(i,pre,vis,dfsvis,newVis)):
#                     res=[]
#                     return res 
#                 newVis.append(i)
#             for x in newVis:
#                 res.append(x)
#         return res[::-1]
                
        
#     def hasCycle(self,node,pre,vis,dfsvis,newVis):
#         vis[node]=1
#         dfsvis[node]=1
#         if(node in pre):
#             for x in pre[node]:
#                 if(vis[x]==0):
#                     if(self.hasCycle(x,pre,vis,dfsvis,newVis)):
#                         return True
#                     newVis.append(x)
#                 elif(dfsvis[x]==1):
#                     return True
#         dfsvis[node]=0
#         return False