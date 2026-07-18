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

class Solution {
    public List<Integer> rightSideView(TreeNode root) {

        int i = 0; 
        List<Integer> dynamicArray = new ArrayList<>();
        if(root == null) return dynamicArray;
        dynamicArray.add(root.val);
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
            TreeNode lastNode = deque.peekLast();
            if (lastNode != null) {
                dynamicArray.add(lastNode.val);
            }
            int j = 0;
            while(i > 0){
                TreeNode current = deque.pollFirst();
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

            i = j;
        }

        return dynamicArray;
    }
}