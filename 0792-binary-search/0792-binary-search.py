class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        first = 0
        last = len(nums) - 1
        middle = (first + last) // 2
        print(middle)
        while first <= last:

            if nums[middle] == target:
                return middle

            elif nums[middle] > target:
                last = middle -1
            elif nums[middle] < target:
                first = middle + 1
            middle = (first + last) // 2
            # print(middle)


        return -1
