class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        first = 0
        second = len(nums) - 1


        while first < second and first is not second:
            mid = (first + second) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                second = mid
            else:
                first = mid 

            if first + 1 == second :
                break

        if nums[first] == target:
            return first 
        elif nums[second] == target:
            return second 
        return -1

        