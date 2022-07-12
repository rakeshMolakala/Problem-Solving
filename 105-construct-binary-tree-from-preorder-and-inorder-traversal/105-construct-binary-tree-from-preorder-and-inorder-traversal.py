# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        track = dict()
        for i in range(len(inorder)):
            track[inorder[i]]  = i
        
        
        def recur(preorder,inorder):
            if(not preorder or not inorder):
                return None
            root = TreeNode(preorder[0])
            index = track[preorder[0]]
            leftTree = self.buildTree(preorder[1:index+1],inorder[0:index])
            rightTree = self.buildTree(preorder[index+1:],inorder[index+1:])
            root.left = leftTree
            root.right = rightTree
            return root
            
        return recur(preorder,inorder)