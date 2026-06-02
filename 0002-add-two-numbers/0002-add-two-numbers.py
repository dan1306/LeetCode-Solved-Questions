# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        
        dummy = ListNode() 
        cur = dummy
        
        carry = 0
        
        while l1 or l2:
            val1 = 0
            if l1 != None:
                val1 = l1.val
            val2 = 0
            if l2 != None:
                val2 = l2.val
                
            sum = val1 + val2 + carry
            carry = sum // 10
            app = sum % 10
            
            nodelist = ListNode()
            nodelist.val = app
            cur.next = nodelist
            cur = cur.next
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2  = l2.next
                
        if carry > 0:
            nodelist1 = ListNode()
            nodelist1.val = carry
            cur.next = nodelist1
            cur = cur.next
        
        return dummy.next
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """