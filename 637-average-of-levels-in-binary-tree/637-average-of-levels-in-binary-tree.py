# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            total = 0
            for i in range(n):
                curr = q.popleft()
                total += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(total/n)
        
        return res