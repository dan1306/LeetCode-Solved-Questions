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

import java.util.ArrayList;
import java.util.List;
 
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> numbers = new ArrayList<>();
        if(root == null) return numbers;
        inAction(root, numbers);
        return  numbers;
    }

    public void inAction(TreeNode root, List<Integer> list){
        if(root.left != null){
          inAction(root.left, list);
        }
        list.add(root.val);
        if(root.right != null){
            inAction(root.right, list);
        }
        return;
    }
}