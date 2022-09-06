# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def postOrder(root):
            if not root:
                return False
            right = postOrder(root.right)
            left = postOrder(root.left)
            if not left:
                root.left = None
            if not right:
                root.right = None
            if (root.left or root.right) and root.val==0:
                return True
            if root.val==1:
                return True
            
        postOrder(root)
        if root.val==0 and not root.left and not root.right:
            return None
        
        return root
                
            