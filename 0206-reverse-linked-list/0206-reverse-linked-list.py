# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        prev = None
        curr = head
        nxt = head.next
        nxtUp= None
        first = 0

        print(nxt.val)

        while nxt != None:

            if first == 0:
                curr.next = None
                nextUp = nxt.next
                nxt.next = curr
                first = 1
            else:
                curr.next = prev
                nextUp = nxt.next
                nxt.next = curr
            prev = curr
            curr = nxt
            nxt = nextUp

        # curr.next = prev
        return curr



    
        