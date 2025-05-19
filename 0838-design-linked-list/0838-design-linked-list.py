class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """

        if((self.size == 0) or (index > self.size) or (index < 0) or (index == self.size) ):
            return -1
        
        if index == 0:
            return self.head.val
        
        if index == (self.size - 1):
            return self.tail.val
        
        
        desired_index = 0

        dummy = self.head

        while desired_index != index:

            dummy = dummy.next
            desired_index += 1
        
        return dummy.val


        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None and self.tail == None:
            nextUp = ListNode(val)

            self.head = self.tail = nextUp
            self.size += 1
        else:
            nextUp = ListNode(val)
           
            nextUp.next = self.head
            self.head = nextUp
            self.size += 1
 
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None and self.tail == None:
            nextUp = ListNode(val)

            self.head = self.tail = nextUp
            self.size += 1
        else:
            nextUp = ListNode(val)
            self.tail.next = nextUp
            self.tail  = self.tail.next 
            self.size += 1
 

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if(index > self.size or index < 0):
            return
        elif(index == self.size):
            self.addAtTail(val)
        elif(index == 0):
            self.addAtHead(val)
        else:
            
            desired_index = 0

            dummy = self.head

            while desired_index !=  index - 1:

                dummy = dummy.next
                desired_index += 1
            
            nextUp = ListNode(val)

            nextUp.next = dummy.next
            dummy.next = nextUp
            self.size += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        print(index)
        print(self.size)

        if(index > self.size or index < 0 or index == self.size):
            return
        
        if index == 0 and self.head == self.tail and self.size == 1:
            self.size -= 1
            self.head = self.tail = None
        elif self.size == 2:
            if index == 0:
                self.head = self.tail
                self.size -= 1
            elif index == 1:
                self.head.next = None
                self.tail = self.head
                self.size -= 1
        else:
            if index == 0:
                self.head = self.head.next
                self.size -= 1
                return
            
            desired_index = 0

            dummy = self.head

            while desired_index !=  index - 1:

                dummy = dummy.next
                desired_index += 1
            
            if(index == (self.size - 1)):
                dummy.next = None
                self.tail = dummy
            else:
                dummy.next = dummy.next.next
            self.size -= 1
        




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)