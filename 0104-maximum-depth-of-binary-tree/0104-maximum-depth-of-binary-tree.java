/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        // int r = 1;
        // int dummmyInt = 1;
        // if(root.left != null){
        int s = maxDepth(root.left);
        int t = maxDepth(root.right);   
        // }

       if(s > t){
        return s + 1;
       } else{
        return t + 1;
       }

    }
}