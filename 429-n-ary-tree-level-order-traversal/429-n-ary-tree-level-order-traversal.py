"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            temp = []
            for i in range(n):
                curr = q.popleft()
                temp.append(curr.val)
                for child in curr.children:
                    q.append(child)
            res.append(temp)
        return res
                    
                    