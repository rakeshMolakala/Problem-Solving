# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        global res
        res = 0
        dic = collections.defaultdict(int)
        self.preOrder(root,dic)
        return res
        
        
    def preOrder(self,root,dic):
        if root:
            dic[root.val]+=1
            if not root.left and not root.right:
                self.check(dic)
            self.preOrder(root.left,dic)
            self.preOrder(root.right,dic)
            dic[root.val]-=1
        
    
    def check(self,dic):
        global res
        count = 0
        for k,v in dic.items():
            if v%2!=0:
                count+=1
        if count<=1:
            res +=1
            