class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if len(nums) == 1 and nums[0] == target:
            return 0

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1

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
            print(middle)


        return -1
