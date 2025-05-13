class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # count = 0
        ans = []
        for j in range(0, 2):
            for i in nums:
                ans.append(i)
            # count += 1;
        return ans