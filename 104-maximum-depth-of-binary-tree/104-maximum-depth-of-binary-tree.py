# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if(root==None):
        #     return 0
        # leftDepth = self.maxDepth(root.left)
        # rightDepth = self.maxDepth(root.right)
        # return max(leftDepth,rightDepth)+1
        
        # BFS 
        if not root:
            return 0
        q = deque()
        q.append(root)
        level= 0
        while(q):
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            level+=1
                
        return level
                
                
                
                
                
                
                
                
                