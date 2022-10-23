class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        self.stack.append(val)
        n = min(self.stack)
        self.minStack.append(n)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.minStack[-1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()