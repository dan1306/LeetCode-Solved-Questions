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
    public TreeNode insertIntoBST(TreeNode root, int val) {

        if(root == null){
            root = new TreeNode(val);
            return root;
        }

        TreeNode copy = root;
        TreeNode pre = null;

        while(copy != null){
            pre = copy;
            if(val <= copy.val){
                copy = copy.left;
            } else {
                copy = copy.right;
            }
        }

        if(val > pre.val){
            pre.right = new TreeNode(val);
        }else {
            pre.left = new TreeNode(val);
        }

        return root;
        
    }
}