class KthLargest(object):

    def __init__(self, k, nums):
        self.nums  = nums
        self.k = k

        """
        :type k: int
        :type nums: List[int]
        """




    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)