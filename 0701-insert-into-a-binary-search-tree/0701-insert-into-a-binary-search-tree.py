# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        
        node = TreeNode(val)
        dummyRoot = root
        
        if root == None:
            root = node
            return root
        
        while dummyRoot:
            if val < dummyRoot.val:
                if dummyRoot.left:
                    dummyRoot = dummyRoot.left
                else:
                    dummyRoot.left = node
                    return root
            elif  val > dummyRoot.val:
                if dummyRoot.right:
                    dummyRoot = dummyRoot.right
                else:
                    dummyRoot.right = node
                    return root
                    
            
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        