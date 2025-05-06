class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if(len(nums) == 0 ):
            return
        

        # if(len(nums) == 1 and nums[0] == val):
        #     nums.remove(val)
        #     return
    
        # if(len(nums) == 2 and nums[0] == val and nums[1] == val):
        #     nums.remove(val)
        #     nums.remove(val)
        #     return
        one = 0
        two = len(nums ) - 1

        while(one != two):

            if(nums[two] == val):
                nums.pop(-1);
                two = len(nums ) - 1;
                continue;


            if(nums[one] == val):
                change_1 = nums[one];
                change_2 = nums[two];

                nums[two] = change_1;
                nums[one] = change_2;
                nums.pop(-1);
                two = len(nums) -1;
            else:
                one+= 1;

        if(len(nums) == 1 and nums[0] == val):
            nums.remove(val)
            return

        # print(nums)

