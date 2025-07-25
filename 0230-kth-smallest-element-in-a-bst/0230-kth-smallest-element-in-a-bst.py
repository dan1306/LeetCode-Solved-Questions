# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        if root == None:
            return []
        
        l = []
        ans = None

        self.recurssionSolution(root, l)
        return l[k - 1]



    def recurssionSolution(self, r, l):

        if r.left:
            self.recurssionSolution(r.left,  l)
        
        l.append(r.val)

        if r.right:
            self.recurssionSolution(r.right,  l)
        
        return
        
        