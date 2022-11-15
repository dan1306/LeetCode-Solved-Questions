class Solution(object):
    def subsets(self, nums):
        
        res = []
        subset = []

        def rec(i):

            if i == len(nums):
              
                res.append(list(subset))
                return

            subset.append(nums[i])
            rec(i + 1)

            subset.pop()
            rec(i + 1)

        rec(0)
        return res


        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        