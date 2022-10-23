class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        
                
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            print(list1.val, list2.val)
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

                
           
            tail.next = None
            
        if list1 != None:
            tail.next = list1
        elif list2 != None:
            tail.next = list2
            
        return dummy.next