class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # set_ = set()

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                min_ = min(i, j)
                max_ = max(i, j)

                # if (min_, max_) in set_:
                #     continue

                if nums[i] + nums[j] == target:
                    return [i, j]
                # set_.add((min_, max_))