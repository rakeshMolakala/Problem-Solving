from collections import deque

#BiDirectional bfs very clever
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        coord = [(2,1),(1,2),(2,-1),(1,-2),(-1,2),(-2,1),(-2,-1),(-1,-2)]
        
        qStart=deque()
        qStart.append((0,0,0))
        disStart=dict()
        disStart[(0,0)]=0
        
        qEnd=deque()
        qEnd.append((x,y,0))
        disEnd=dict()
        disEnd[(x,y)]=0
        
        
        while(True):
            xStart,yStart,startSteps = qStart.popleft()
            if (xStart,yStart) in disEnd:
                return disEnd[(xStart,yStart)] + startSteps
            
            xEnd,yEnd,endSteps = qEnd.popleft()
            if (xEnd,yEnd) in disStart:
                return endSteps + disStart[xEnd,yEnd]
            
            for coox,cooy in coord:
                nextXStart = xStart + coox
                nextYStart = yStart + cooy
                
                if((nextXStart,nextYStart) not in disStart):
                    qStart.append((nextXStart,nextYStart,startSteps+1))
                    disStart[(nextXStart,nextYStart)] = startSteps+1
                    
                
                nextXEnd = xEnd + coox
                nextYEnd = yEnd + cooy
                
                if((nextXEnd,nextYEnd) not in disEnd):
                    qEnd.append((nextXEnd,nextYEnd,endSteps+1))
                    disEnd[(nextXEnd,nextYEnd)] = endSteps+1
    
    
    
   # Normal BFS
# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         coord = [(2,1),(1,2),(2,-1),(1,-2),(-1,2),(-2,1),(-2,-1),(-1,-2)]
#         visited = set()
#         q=deque()
#         q.append((0,0,0))
#         visited.add((0,0)) 
#         currSteps = 0
        
#         while(q):
#             currX,currY,currSteps = q.popleft()
#             if(currX==x and currY==y):
#                 return currSteps
#             for coor in coord:
#                 if((currX+coor[0],currY+coor[1]) not in visited):
#                     q.append((currX+coor[0],currY+coor[1],currSteps+1))
#                     visited.add((currX+coor[0],currY+coor[1]))
                    
        # return currSteps
                
        
        