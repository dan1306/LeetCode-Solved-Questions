class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        
        if len(nums) == 1:
            return[]

        dummyList = sorted(nums);

        l_index = 0;
        r_index = len(nums) - 1;

        while dummyList[l_index] + dummyList[r_index] != target and l_index != r_index:

            if dummyList[l_index] + dummyList[r_index] > target:
                r_index -= 1;
            elif dummyList[l_index] + dummyList[r_index] < target:
                l_index += 1;

        if l_index != r_index and dummyList[l_index] * 2 == target:
            placeholder = nums.index(dummyList[l_index]);
            nums[placeholder] = "i am just here"
            return [placeholder, nums.index(dummyList[r_index])];
        return [nums.index(dummyList[l_index]), nums.index(dummyList[r_index])];
        