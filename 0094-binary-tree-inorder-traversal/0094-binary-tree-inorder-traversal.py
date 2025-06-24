# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []
        
        l = []

        self.recurssionSolution(root, l)
        return l


        


    
    def recurssionSolution(self, r, l):

        if r.left:
            self.recurssionSolution(r.left,  l)
        
        l.append(r.val)

        if r.right:
            self.recurssionSolution(r.right,  l)
        
        return
        
