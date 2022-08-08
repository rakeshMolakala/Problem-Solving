# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        
        
        def height(node):
            if(not node):
                return 0
            leftH = height(node.left)
            rightH = height(node.right)
            currH = 1+max(leftH,rightH)
            dic[currH].append(node.val)
            return currH
        
        height(root)
        res = []
        for x in dic.values():
            res.append(x)
        return res
        