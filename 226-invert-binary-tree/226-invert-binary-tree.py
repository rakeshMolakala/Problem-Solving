# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = root
        def recur(root):
            if(not root):
                return 
            temp = root.left
            root.left = root.right
            root.right = temp
            recur(root.left)
            recur(root.right)
        
        recur(root)
        return res
            
                
            
            
        