# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True
        if not root:
            return False
        if not subroot:
            return True
        p1 = self.sameTree(root,subroot)
        if(not p1):
            return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
        else:
            return True
        
        
    def sameTree(self,root1,root2):
        if(root1==None and root2==None):
            return True
        if(root1==None or root2==None):
            return False
        return root1.val==root2.val and self.sameTree(root1.left,root2.left) and self.sameTree(root1.right,root2.right)
            