class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0, len())

        if (len(nums) == 0):
            return 0;
        if (len(nums) == 1):
            return 1;

        k = 1;
        element_at_index = nums[0]
        curr = 1;
        print("element at curr " + str(curr) + " " + str(nums[curr]));

        while(curr < len(nums)):
            print("element at curr " + str(curr) + " " + str(nums[curr]));
            if (nums[curr] == element_at_index):
                print("popping " + str(nums[curr]))
                nums.pop(curr);
            else:
                element_at_index = nums[curr];
                curr += 1;
                k += 1;