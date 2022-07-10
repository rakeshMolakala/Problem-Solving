# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recur(root):
            if(root==None or root==p or root==q):
                return root
            left = recur(root.left)
            right = recur(root.right)
            if(left==None):
                return right
            elif(right==None):
                return left
            else:
                return root
        return recur(root)