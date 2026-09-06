class KthLargest(object):

    def __init__(self, k, nums):
        self.arr = [0]
        self.numOfElements = 0
        self.addAtIndex = 1
        self.k = k 

        for i in nums:
            self.init(i)


        """
        :type k: int
        :type nums: List[int]
        """
    
    def init(self, val):
        
        if self.numOfElements == 0:
            self.arr.append(val)
            self.numOfElements += 1
            self.addAtIndex += 1
        elif self.numOfElements == self.k:
            if val > self.arr[1] and self.k >= 1:
                self.arr[1] = val

                starting_index = 1
                left_child = 2 * starting_index
                right_child = 2 * starting_index + 1

                while left_child <= self.k:
                    
                    if right_child > self.k:
                        if self.arr[left_child] < self.arr[starting_index]:
                            child = self.arr[left_child]
                            parent = self.arr[starting_index]

                            self.arr[left_child] = parent
                            self.arr[starting_index] = child

                        break
                    else:

                        min_index = left_child if self.arr[left_child] <= self.arr[right_child] else right_child

                        if self.arr[min_index] < self.arr[starting_index]:
                            child = self.arr[min_index]
                            parent = self.arr[starting_index]
                            self.arr[min_index] = parent
                            self.arr[starting_index] = child
                        else:
                            break
                    
                        starting_index = min_index
                        left_child = 2 * starting_index
                        right_child = 2 * starting_index + 1

        elif self.numOfElements < self.k:
            self.arr.append(val)
            # copy = self.arr 
            parent_index = (self.addAtIndex ) // 2
            target = self.addAtIndex
            while parent_index >= 1 and self.arr[target] < self.arr[parent_index]:
                
                child = self.arr[target]
                parent = self.arr[parent_index]

                self.arr[parent_index] = child
                self.arr[target] = parent

                target = parent_index
                parent_index = target // 2

            self.numOfElements+=1
            self.addAtIndex +=1




    def add(self, val):
        # print(val)
        self.init(val)
        # print(self.arr)
        # print("\n")
        # print self.arr[self.k]
        if self.numOfElements == self.k:
            return self.arr[1]
        

        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)