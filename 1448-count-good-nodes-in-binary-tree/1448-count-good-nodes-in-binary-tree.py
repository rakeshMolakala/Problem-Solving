# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global res
        res = 0
        
        def preOrder(root,maxi):
            if root:
                global res
                if root.val>=maxi:
                    res+=1
                preOrder(root.left,max(maxi,root.val))
                preOrder(root.right,max(maxi,root.val))
        
        preOrder(root,-math.inf)
        return res
            