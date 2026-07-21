# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def hasPathSum(self, root, targetSum):
        self.res = 0
        
        return self.sumItUp(root, targetSum)

    def sumItUp(self, root, targetSum):
        if root == None: 
            return False
        self.res += root.val
        
        if root.right == None and root.left == None:
            if self.res == targetSum:
                return True
            
        if self.sumItUp(root.left, targetSum):
            return True
        if self.sumItUp(root.right, targetSum):
            return True
        
        self.res -= root.val
        return False
        
       
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        