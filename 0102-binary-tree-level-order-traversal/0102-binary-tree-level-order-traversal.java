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
import java.util.ArrayDeque;
import java.util.List;
import java.util.Deque;


import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        int i = 0; 
        List<List<Integer>> dynamicArray = new ArrayList<>();
        if(root == null) return dynamicArray;
        List<Integer> r = new ArrayList<>();
        r.add(root.val);
        dynamicArray.add(r);
        Deque<TreeNode> deque = new ArrayDeque<>();
        // deque.addLast(root);
        if(root.left != null) {
            deque.addLast(root.left);
            i+=1;
        }
        if(root.right != null) {
            deque.addLast(root.right);
            i+=1;
        }
        while(!deque.isEmpty()){
            int j = 0;
            List<Integer> rs = new ArrayList<>();
            while(i > 0){
                TreeNode current = deque.pollFirst();
                rs.add(current.val);
                if(current.left != null){
                    deque.addLast(current.left);
                    j+=1;
                }
                if(current.right != null){
                    deque.addLast(current.right);
                    j+=1;            
                }
                i-=1;
            }
            dynamicArray.add(rs);
            i = j;
        }

        return dynamicArray;
    }
}