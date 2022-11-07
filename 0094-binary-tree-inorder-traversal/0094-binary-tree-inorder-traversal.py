# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        
        if root is None:
            return []
        
        def recur(list, obj):
            if obj.left:
                recur(list, obj.left)
            list.append(obj.val)
            if obj.right:
                recur(list, obj.right)
            return list
        
        return recur([], root)
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        