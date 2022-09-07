# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        
        def preOrder(root,maxi,res):
            if root:
                if root.val>=maxi:
                    res+=1
                left = preOrder(root.left,max(maxi,root.val),0) 
                right = preOrder(root.right,max(maxi,root.val),0)
                return res + left + right
            else:
                return 0
        
        return preOrder(root,-math.inf,0)
            