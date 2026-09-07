class Node:

  def __init__(self, val=0, key=0, prev=None, next=None):
    self.val = val
    self.key = key
    self.prev = prev
    self.next = next

class DoublyLinkedList:

    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = size

    def reached_cap(self):
        return self.capacity == self.size


    def remove_oldest_node(self):
        if self.reached_cap() and self.capacity > 0:
            returnKey = self.head.key
            if self.size == 1:
                self.head = None
                self.tail = self.head
        
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return returnKey


    def append(self, node_):
        # if self.reached_cap() and self.capacity > 0:

        new_node = node_

        if not self.head:
            # First element ever added
            self.head = new_node
            self.tail = new_node
        else:
            # Link to current tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node  # Move tail forward
        self.size += 1

    def exist_append(self, node_):
   
        if self.head != self.tail and self.tail != node_:
            if node_.prev == None and node_ == self.head:
                nxt_node = node_.next
                nxt_node.prev = None
                self.head = nxt_node
                node_.next = None
                node_.prev = self.tail
                self.tail.next = node_
                self.tail = node_
                
            
            else:
                prev_node = node_.prev
                next_node = node_.next
                prev_node.next = node_.next
                next_node.prev = node_.prev

                node_.next = None
                node_.prev = self.tail

                self.tail.next = node_
                self.tail = node_




class LRUCache(object):

    def __init__(self, capacity):
        self.hash = {}
        self.capacity = capacity
        self.doubly = DoublyLinkedList(capacity)

        """
        :type capacity: int
        """
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.hash:
            self.doubly.exist_append(self.hash[key])
            return self.hash[key].val
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        if key not in self.hash:
            if self.doubly.reached_cap():
                x = self.doubly.remove_oldest_node()
                del self.hash[x]

            
            node_ = Node(value, key)
            self.doubly.append(node_)
            self.hash[key] = node_
        
        else:
            self.hash[key].val = value
            self.doubly.exist_append(self.hash[key])

