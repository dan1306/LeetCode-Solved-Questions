# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return ListNode().next
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
                        
        dummy = ListNode()
        tail = dummy
        first  = 0

        while list1 and list2:

            if(list1.val > list2.val):
                if(first == 0):
                    tail.val = list2.val
                    first = 1
                    list2 = list2.next
                    continue


                dono = ListNode()
                dono.val = list2.val
                tail.next = dono
                tail = tail.next

                list2 = list2.next
            else:
                if(first == 0):
                        tail.val = list1.val
                        first = 1
                        list1 = list1.next
                        continue

            
                dono = ListNode()
                dono.val = list1.val
                tail.next = dono
                tail = tail.next
                list1 = list1.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy
        