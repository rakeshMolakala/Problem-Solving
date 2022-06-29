# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res =[]
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp={0:[],1:[TreeNode()]}
        return self.recur(n,dp)
        
        
    def recur(self,n,dp):
        if(n in dp):
            return dp[n]
        

        res  = []
        for l in range(n):
            r = n-l-1
            lTrees = self.recur(l,dp)
            rTrees = self.recur(r,dp)
            
            for x in lTrees:
                for y in rTrees:
                    res.append(TreeNode(0,x,y))
                    
        dp[n] = res
        return res
        
        
        
        
        