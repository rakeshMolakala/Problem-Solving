# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        track = collections.defaultdict(list)
        rowcol_track = dict()
        q = collections.deque()
        q.append(root)
        rowcol_track[root] = (0,0)
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                curr_row,curr_col = rowcol_track[curr]
                track[curr_col].append(curr)
                if curr.left:
                    q.append(curr.left)
                    rowcol_track[curr.left] = (curr_row+1,curr_col-1)
                if curr.right:
                    q.append(curr.right)
                    rowcol_track[curr.right] = (curr_row+1,curr_col+1)
                
        heap = []
        res = []
        for k,v in track.items():
            v.sort(key=lambda a: (rowcol_track[a][0],a.val))
            heap.append((k,v))
        heapq.heapify(heap)
        while heap:
            k,v = heapq.heappop(heap)
            temp_list = []
            for node in v:
                temp_list.append(node.val)
            res.append(temp_list)
        return res
                
                
                