class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        setOn = set(nums);

        returnThisNum = 0;

        for i in setOn:
            if i - 1 in setOn:
                continue;

            placeholder = i + 1;

            increment = 1;
            
            while placeholder in setOn:
                increment += 1;
                placeholder += 1;
            
            if increment > returnThisNum:
                returnThisNum = increment;

        return returnThisNum;
