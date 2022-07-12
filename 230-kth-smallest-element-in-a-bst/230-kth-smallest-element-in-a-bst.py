# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = [0]
        ans = [0] 
        
        def inorder(root):
            if root:
                inorder(root.left)
                count[0] +=1
                if(count[0]==k):
                    ans[0] = root.val
                    return
                inorder(root.right)
                
        inorder(root)
        return ans[0]