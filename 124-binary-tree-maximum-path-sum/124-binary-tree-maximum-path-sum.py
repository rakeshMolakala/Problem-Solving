# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global res
        res = -math.inf
        
        def recur(root):
            if(not root):
                return 0
            leftMax = max(0,recur(root.left))
            rightMax = max(0,recur(root.right))
            global res
            res = max(res,leftMax+rightMax+root.val)
            return root.val+max(leftMax,rightMax)
        
        recur(root)
        return res