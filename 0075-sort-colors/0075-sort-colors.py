class Solution(object):
    def sortColors(self, nums):
        for i in range(1, len(nums)):

            for x in range(0, i):

                if nums[i] < nums[x]:
                    nums.insert(x, nums.pop(i))
                    break


        return(nums)


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        