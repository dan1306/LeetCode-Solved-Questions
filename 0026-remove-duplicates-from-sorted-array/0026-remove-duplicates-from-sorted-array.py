class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0, len())

        if(len(nums) == 0):
            return 0;
        if(len(nums) == 1):
            return 1;
        
        k = 1;
        element_at_index = nums[0]
        curr = 1;
        while(curr < len(nums)):
            if(nums[curr] == element_at_index):
                nums[curr] = " ";
                curr+=1;
            else:
                element_at_index = nums[curr];
                curr+=1;
                k+=1;
        # print("ans is = " + str(k) )
        # return k
        
        while " " in nums:
            nums.remove(" ");
