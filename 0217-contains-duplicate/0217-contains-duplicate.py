class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        empty = set()
        for i in nums:
            if i in empty:
                return True
            empty.add(i)
        return False
        