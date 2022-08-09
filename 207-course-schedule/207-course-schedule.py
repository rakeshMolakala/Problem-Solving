class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return False
        
        coursesDone = 0
        while(q):
            curr = q.popleft()
            coursesDone += 1 
            for neigh in adj[curr]:
                indegree[neigh]-=1
                if(indegree[neigh]==0):
                    q.append(neigh)
        return coursesDone == numCourses
                    
            
        
        
        
        
    
    
    
    
    
    
    
    
    
    
#     global track
#     track=[]
    
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         pre = dict()
#         if(len(prerequisites)<=1):
#             return True
#         for x in prerequisites:
#             if(x[1] in pre):
#                 pre[x[1]].append(x[0])
#             else:
#                 pre[x[1]]=[x[0]]
                
#         vis=[0]*numCourses
#         dfsvis=[0]*numCourses
#         for i in range(numCourses):
#             if(vis[i]==0):
#                 if(self.hasCycle(i,pre,vis,dfsvis)):
#                     # print(track)
#                     # ans=0
#                     # for i in range(len(track)):
#                     #     if(track[i]==track[-1]):
#                     #         ans=i
#                     #         break
#                     # print(track[ans:-1])
#                     return False
#         return True
                
        
#     def hasCycle(self,node,pre,vis,dfsvis):
#         vis[node]=1
#         # track.append(node)
#         dfsvis[node]=1
#         if(node in pre):
#             for x in pre[node]:
#                 if(vis[x]==0):
#                     if(self.hasCycle(x,pre,vis,dfsvis)):
#                         return True
#                 elif(dfsvis[x]==1):
#                     # track.append(x)
#                     return True
#         dfsvis[node]=0
#         # track.pop()
#         return False
        
                
            
                
        
        