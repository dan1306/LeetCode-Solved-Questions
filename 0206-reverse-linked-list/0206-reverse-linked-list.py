class Solution(object):
    def reverseList(self, head):
        
        dummy = ListNode()
        tail = dummy
        
        arr= []
        
        while head: 
            arr.append(head)
            head = head.next 
        
        num = -1
    
    
        for i in range(0, len(arr)):

            tail.next = arr[num]
            tail = tail.next
            tail.next = None
            num -= 1

        print(dummy)
        return dummy.next
        