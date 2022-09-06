# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        track = collections.defaultdict(list)
        col_track = dict()
        q = collections.deque()
        q.append(root)
        col_track[root] = 0
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                curr_col = col_track[curr]
                track[curr_col].append(curr.val)
                if curr.left:
                    q.append(curr.left)
                    col_track[curr.left] = curr_col-1
                if curr.right:
                    q.append(curr.right)
                    col_track[curr.right] = curr_col+1
        
        heap = []
        res = []
        for k,v in track.items():
            heap.append((k,v))
        heapq.heapify(heap)
        while heap:
            k,v = heapq.heappop(heap)
            res.append(v)
        return res 
                
                 