# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recur(start,end):
            if(start>end):
                return None
            middle = (start+end)//2
            root = TreeNode(nums[middle])
            root.left = recur(start,middle-1)
            root.right = recur(middle+1,end)
            return root
        
        return recur(0,len(nums)-1)