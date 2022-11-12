"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        
        if not root:
            return []
        
        return self.ans(root, [])
        
        
        
    def ans(self, tree, arr):
        
#         for i in tree.children:
#             print i.val

        
        if tree.children:
            for i in tree.children:
               self.ans(i, arr)
            
        arr.append(tree.val)
            
        return arr
    
        # if tree.left:
        #     self.ans(tree.left, arr)
        # if tree
        """
        :type root: Node
        :rtype: List[int]
        """
        