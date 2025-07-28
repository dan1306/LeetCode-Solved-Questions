class ListNode:
    def   __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr = ListNode(homepage)
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        newUrl = ListNode(url, None, self.curr)

        self.curr.next = newUrl
        self.curr = self.curr.next

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        # returnMe = None
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return  self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)