# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def recur(root,lower,upper):
            if not root:
                return True
            if root.val<=lower or root.val>=upper:
                return False
            if not recur(root.left,lower,root.val):
                return False
            if not recur(root.right,root.val,upper):
                return False
            return True
        
        return recur(root,-math.inf,math.inf)