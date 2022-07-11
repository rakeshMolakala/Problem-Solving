# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def inorder(root1,root2):
            if(root1==None):
                return root2==None
            elif(root2==None):
                return root1==None
            elif(root1==None and root2==None):
                return True
            return root1.val==root2.val and inorder(root1.left,root2.left) and inorder(root1.right,root2.right)
        
        return inorder(p,q)