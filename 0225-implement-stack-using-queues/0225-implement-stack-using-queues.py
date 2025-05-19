class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyStack(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if self.size == 0:
            self.head = self.tail = ListNode(x)
        else:
            dummy =  ListNode(x)
            dummy.prev = self.tail
            self.tail.next = ListNode(x)
            self.tail = dummy
        self.size += 1
        

    def pop(self):
        """
        :rtype: int
        """
        if self.size == 1:
            self.size -=1
            returnMe = self.head
            self.head = self.tail = None
            return returnMe.val
        elif self.size != 0 and self.size > 1:
            returnMe = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return returnMe.val
        

    def top(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return 
        return self.tail.val

        

    def empty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()