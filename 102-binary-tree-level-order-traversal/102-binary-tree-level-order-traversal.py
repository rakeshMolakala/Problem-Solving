# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        res = []
        q = deque()
        q.append(root)
        
        while(q):
            n = len(q)
            temp = []
            for i in range(n):
                curr = q.popleft()
                temp.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            res.append(temp)
        return res
                
        
        