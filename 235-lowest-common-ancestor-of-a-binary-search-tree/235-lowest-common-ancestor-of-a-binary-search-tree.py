# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = min(p.val,q.val)
        b = max(p.val,q.val)
        
        curr=root
        while(curr):
            if(not curr):
                break
            if(a<=curr.val<=b):
                return curr
            if(b<curr.val):
                curr=curr.left
            if(a>curr.val):
                curr=curr.right
                
                
                
        
        
        