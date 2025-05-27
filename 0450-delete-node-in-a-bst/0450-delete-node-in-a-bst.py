# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return
        pre = None
        curr = root
        whchDirection = None

        while curr is not None:
            if key > curr.val:
                pre = curr
                curr = curr.right
            elif key < curr.val:
                pre = curr
                curr = curr.left
            elif curr.val == key:
                if pre is not None and pre.right is not None and pre.right.val == key:                    
                    whchDirection = "right"
                else:
                    whchDirection = "left"
                break
        
        if curr == None:
            return root

        if pre is not None:
            if curr.right == None and curr.left == None:
                if whchDirection == "left":
                    pre.left = None
                else:
                    pre.right = None
            elif curr.right is not None and curr.left == None:
                if whchDirection == "left":
                    pre.left = curr.right
                else:
                    pre.right = curr.right
            elif curr.left is not None and curr.right == None:
                if whchDirection == "left":
                    pre.left = curr.left
                else:
                    pre.right = curr.left
            else:
                nxtCur = curr.right
                if nxtCur.left == None and nxtCur.right == None:
                    curr.val = nxtCur.val
                    curr.right = None
                elif nxtCur.left == None and nxtCur.right is not None:
                    curr.val = nxtCur.val
                    curr.right = nxtCur.right

                else:
                    prePre = None
                    while nxtCur.left is not None:
                        prePre = nxtCur
                        nxtCur = nxtCur.left
                    if nxtCur.right == None:
                        curr.val = nxtCur.val
                        prePre.left = None
                    else:
                        curr.val = nxtCur.val
                        prePre.left = nxtCur.right
        else:
            if curr.left == None and curr.right == None:
                root = None
            elif curr.right is not None and curr.left == None:
                root = root.right
            elif curr.left is not None and curr.right == None:
                root = root.left
            else:
                nxtCur = curr.right
                if nxtCur.left == None and nxtCur.right == None:
                    curr.val = nxtCur.val
                    curr.right = None
                elif nxtCur.left == None and nxtCur.right is not None:
                    curr.val = nxtCur.val
                    curr.right = nxtCur.right
                else:
                    prePre = None
                    while nxtCur.left is not None:
                        prePre = nxtCur
                        nxtCur = nxtCur.left
                    if nxtCur.right == None:
                        curr.val = nxtCur.val
                        prePre.left = None
                    else:
                        curr.val = nxtCur.val
                        prePre.left = nxtCur.right

        return root



        