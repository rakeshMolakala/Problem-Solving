/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int pVal = Math.min(p.val,q.val);
        int qVal = Math.max(p.val,q.val);
        return Recur(root,pVal,qVal);
    }
        
        
    public TreeNode Recur(TreeNode root, int p, int q){
        if(p<root.val && root.val<q){
            return root;
        }
        else if(p>root.val){
            return Recur(root.right,p,q);
        }
        else if(root.val>q){
            return Recur(root.left,p,q);
        }
        else if(root.val==p || root.val==q){
            return root;
        }
        return null;
    }
        
       
    
}