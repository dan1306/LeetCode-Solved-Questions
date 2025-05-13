class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        ans = []
        while count < 2:
            for i in nums:
                ans.append(i)
            count += 1;
        return ans