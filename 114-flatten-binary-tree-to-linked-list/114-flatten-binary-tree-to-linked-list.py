# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        
        st = []
        st.append(root)
        
        while(len(st)>0):
            curr = st.pop()
            if(curr.right):
                st.append(curr.right)
            if(curr.left):
                st.append(curr.left)
            if(len(st)>0):
                curr.right = st[-1]
            curr.left = None
        