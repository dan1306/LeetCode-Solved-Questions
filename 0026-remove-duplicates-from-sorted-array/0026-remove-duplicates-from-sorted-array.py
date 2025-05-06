class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) == 0):
            return 0;
        if (len(nums) == 1):
            return 1;

        pointer_one = 0;
        pointer_two = 0;
        i_am_unique = " ";
        k = 0

        while(pointer_one < len(nums)):
            if(pointer_one == 0):
                i_am_unique = nums[pointer_one];

                pointer_two +=1;
                k += 1;
            else:
                if(i_am_unique != " " and i_am_unique != nums[pointer_one]):
                    i_am_unique = nums[pointer_one];
                    nums[pointer_two] = i_am_unique;
                    k+=1;
                    pointer_two+=1;
            pointer_one += 1;

        while(len(nums) != k):
            nums.pop(-1)

        print(nums)
