# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        res = 0
        
        def sumItUp(root, res):
            if root == None: 
                return False
            res += root.val
            
            if root.right == None and root.left == None:
                if res == targetSum:
                    return True
                
            if sumItUp(root.left, res):
                return True
            if sumItUp(root.right, res):
                return True
            
            res -= root.val
            return False
        
        return sumItUp(root, res)
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        