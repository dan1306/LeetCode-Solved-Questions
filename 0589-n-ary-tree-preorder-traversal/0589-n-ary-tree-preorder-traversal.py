"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        
        if not root:
            return []
        
        return self.ans(root, [])
        
    
    def ans(self, lis, arr):
        
        arr.append(lis.val)
        
        if lis.children:
            for i in lis.children:
                self.ans(i, arr)
                
        return arr
        """
        :type root: Node
        :rtype: List[int]
        """
        